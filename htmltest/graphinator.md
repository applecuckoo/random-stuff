# Mermaid Graphinator

> Idea from [NumWorks](https://www.numworks.com/resources/engineering/software/#discover-epsilons-architecture)

```mermaid
graph TD
      a[Apps - Calculation, Graph, etc.] --> b[Escher - GUI Toolkit]
      a --> c[Poincaré - Mathematical engine]
      b --> d[Kandinsky - Graphics Engine]
      d --> e[Ion - Hardware abstraction layer]
      b --> e
```