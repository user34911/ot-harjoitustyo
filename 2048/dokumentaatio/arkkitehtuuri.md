# Arkkitehtuurikuvaus
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
## Päätoiminnallisuudet
### Laattojen liikuttaminen
Kun näppäimstöllä painaa jotakin liikkumisnappia suorittaa sovellus seuraavasti pienin eroin suunnasta riippuen:
```mermaid
sequenceDiagram
  actor User
  participant GameLoop
  participant Grid
  User->>GameLoop: click "d" or "rightarrow"
  GameLoop->>Grid: move_right()
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
    Grid->>Cell: cell.tile = True
  else if cell has no tile
    Grid->>Cell: cell.tile = False
  end
  end
  opt if tiles moved
  Grid->>Grid: _spawn_tile()
  Grid->>Grid: pick random spawn_cell from cells
  Grid->>+Tile: Tile(cell.size, [2, 4], spawn_cell x, spawn_cell y)
  Tile->>Cell: spawn_cell.tile = True
  Tile->>-Tile: _draw_image()
  Grid->>Grid: tiles.add(tile), all_sprites.add(tile)
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
