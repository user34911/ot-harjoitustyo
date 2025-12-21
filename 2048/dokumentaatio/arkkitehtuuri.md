# Arkkitehtuurikuvaus
## Rakenne
Ohjelman koodi on jaettu hakemistoihin, missä _sprites_ hakemistossa on _Sprite_ oliot, _ui_ hakemistossa käyttöliittymään liittyvä koodi, _leaderboard_ hakemistossa tulostaulukko, ja sen kanssa interaktivoivat funktiot ja muu koodi on päähakemistossa.

## Käyttöliittymä
Käyttöliittymä sisältää kaksi päänäkymää ja usean alinäkymän:
- Peliruudukko
  - Peli ohi näkymä
- Päävalikko
  - Tulostaulukko
    - 4x4 Normaali
    - 4x4 Ajastettu
  - Pelin aloitusasetukset
    - Ruudukon koko
    - Pelimuoto 
  - Käyttäjänimen asetusnäkymä

Kummatkin päänäkymistä ovat oma luokkansa ja vastaavasti alinäkymät sisältyvät päänäkymän luokkaan. Molemmilla näkymillä on oma silmukkansa joiden välillä pääsilmukka vaihtelee vaihdellen näkymää.

## Sovelluslogiikka
Sovellus rakentuu pääsilmukasta, joka hallinoi suoritetaanko peli-, vai päävalikkosilmukkaa
```mermaid
classDiagram
    main "1" -- "1" GameLoop
    main "1" -- "1" MenuLoop
    MenuLoop "1" -- "1" Menu
    MenuLoop "1" -- "1" MenuRenderer
    Menu "1" -- "1" leaderboard
    GameLoop "1" -- "1" Grid
    GameLoop "1" -- "1" Clock
    GameLoop "1" -- "1" EventQueue
    GameLoop "1" -- "1" Renderer
    Grid "1" -- "*" Cell
    Grid "1" -- "*" Tile
    Cell "1" -- "1" Tile
    Grid "1" -- "1" Score
    Grid "1" -- "4" Borders
  ```

## Tietojen pysyväistallennus
Sovellus tallentaa tulostaulukon pysyvästi paikallisesti CSV-tiedostoon. Tietojen tallentamisesta vastaa `leaderboard.py` tiedoston funktio `add_score_to_lb` ja noutamisesta `get_leaderboard`.

### Tiedostot
Sovellus tallentaa pelien tulokset tiedostoon `leaderboard.csv`.
Tiedostossa tulokset ovat muodossa
```
guest,2303
teemu,21380
jare,9572
```
Eli `{käyttäjänimi},{tulos}`


## Päätoiminnallisuudet
### Laattojen liikuttaminen
Ohjelman suoritus, kun käyttäjä haluaa liikuttaa laattoja oikealle
```mermaid
sequenceDiagram
  actor User
  participant GameLoop
  participant Grid
  User->>GameLoop: click "d" or "rightarrow"
  GameLoop->>Grid: move(Direction.RIGHT)
  loop while movable tiles
  Grid->>Grid: _get_movable_tiles(Direction.RIGHT)
  loop for every movable tile
  Grid->>+Tile: tile.rect.move_ip(cell.size, 0)
  end
  Grid->>Grid: _combine_tiles(tile)
  end
  Grid->>Grid: _update_cell_tiles()
  loop for every cell
  alt if cell has tile
    Grid->>Cell: cell.tile = Tile
  else if cell has no tile
    Grid->>Cell: cell.tile = None
  end
  end
  opt if tiles moved
  Grid->>Grid: _spawn_tile()
  Grid->>Grid: pick random spawn_cell from cells
  Grid->>+Tile: Tile(cell.size, [2, 4], spawn_cell x, spawn_cell y)
  Tile->>Cell: spawn_cell.tile = Tile
  Tile->>-Tile: _draw_image()
  Grid->>Grid: objects[Object.TILE].add(Tile)
  end
  Grid->>Grid: _unlock_all_tiles()
  loop for every tile
  Grid->>Tile: tile.lock = False
  end
  GameLoop->>Grid: update()
  participant Renderer
  GameLoop->>Renderer: render()
  GameLoop->>GameLoop: clock_tick(60)
  GameLoop->>User: Tile has moved on screen
  ```
### Pelin aloittaminen
Ohjelman suoritus, kun käyttäjä aloittaa ajastetun pelin oletus ruudukkokoolla
```mermaid
sequenceDiagram
  actor User
  participant MenuLoop
  User->>MenuLoop: click "Start" button
  MenuLoop->>MenuLoop: _handle_main_menu_event(event)
  MenuLoop->>MenuLoop: _screens.[MenuScreen.START_OPTIONS].container.show()
  MenuLoop->>User: start options visible
  User->>MenuLoop: check "timed mode" box
  User->>MenuLoop: click "Start" button
  MenuLoop->>MenuLoop: _handle_start_option_event(event)
  MenuLoop->>Options: change(Option.MODE, Mode.TIMED)
  Options->>Options: _option[Option.MODE] = Mode.TIMED
  MenuLoop->>Options: change(Option.GRID_SIZE, 4)
  Options->>Options: _option[Option.GRID_SIZE] = 4
  MenuLoop->>Options: change(Option.STATE, State.GAME)
  Options->>Options: _option[Option.STATE] = State.GAME
  MenuLoop->>Index:
  Index->>Options: get(Option.STATE)
  Options->>Index:State.GAME
  create participant Game
  Index->>Game: start()
  Game->>Game: _initialise_game()
  create participant Grid
  Game->>Grid: Grid(grid_size, cell_size, position, mode)
  create participant GameLoop
  Game->> GameLoop: GameLoop(grid, renderer, options, queue, clock)
  Game->>GameLoop: start()
  GameLoop->>User: game is running
 ```
### Pelin päättyminen
Ohjelman suoritus, kun peli loppuu peliruudukon täyttyessä
```mermaid
sequenceDiagram
  actor User
  participant GameLoop
  User->>GameLoop: grid gets full
  participant Grid
  GameLoop->>+Grid: get_game_state()
  Grid->>-GameLoop: Game.LOST
  GameLoop->>GameLoop: _game_over(Game.LOST)
  GameLoop->>+Grid: get_game_mode()
  Grid->>-GameLoop: Mode.STANDARD
  GameLoop->>GameLoop: _submit_to_leaderboards(Mode.STANDARD)
  GameLoop->>+Options: get(Option.USER)
  Options->>-GameLoop: username
  GameLoop->>+Grid: score.get_score()
  Grid->>-GameLoop: score
  GameLoop->>GameLoop: add_to_leaderboard([username, score], Mode.STANDARD)
  GameLoop->>User: "Game Over" text visible
  User->>GameLoop: press "esc"
  GameLoop->>Options: change(Option.STATE, State.MENU)
  GameLoop->>Index:
  Index->>+Options: get(Option.STATE)
  Options->>-Index: State.MENU
  create participant Menu
  Index->>Menu: start()
  Menu->>Menu: _initialise_menu()
  create participant MenuLoop
  Menu->>MenuLoop: MenuLoop(screens, manager, renderer, options)
  Menu->>MenuLoop: start()
  MenuLoop->>User: main menu visible
```
