# Arkkitehtuurikuvaus
## Sovelluslogiikka
```mermaid
  classDiagram
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
