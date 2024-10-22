# BFS Keyword Web Crawler

This is a Python-based web crawler that uses **Breadth-First Search (BFS)** to explore web pages and search for a specific keyword on those pages.

## Usage:
1. **Enter the Start URL**: Provide the URL where the crawler should begin. Ensure the URL is in the format `https://example.com`.

2. **Enter the Keyword**: Provide the keyword that you want to search for on the web pages.

3. **Crawler Execution**: The crawler will visit each page and look for the keyword, reporting the first URL where it finds the keyword or stopping after the specified depth/page limit.

### Example:
```bash
Enter the start URL: https://example.com
Enter the keyword to search: computer systems
```

The crawler will traverse the website starting at `https://example.com`, visiting pages up to the specified depth or maximum number of pages, and search for the keyword "computer systems".

## Parameters:
- `start_url`: The URL where the crawl begins.
- `keyword`: The word or phrase the crawler looks for on each page.
- `max_depth` (default = 3): Maximum depth of link traversal.
- `max_pages` (default = 100): Maximum number of pages to visit.

## Error Handling:
- **Timeouts**: If a page takes too long to load, the crawler skips the page after 10 seconds.
- **Request Failures**: If a page cannot be accessed, the crawler reports the error and moves to the next URL.

## Notes:
- Ensure the start URL is properly formatted (`https://` or `http://`).
- This crawler only processes text content of web pages.

# DFS-Based Course Scheduler

This project implements a **Depth-First Search (DFS)** algorithm-based Topological Sorting to determine the valid order in which courses can be completed, considering their prerequisites.

## Usage:
1. **Input Courses**: The script contains an example list of courses and their prerequisites, but these can be modified as needed.

2. **Check Results**: If there is a cycle, the program will output:
   ```
   There is a cycle. Cannot complete the courses.
   ```
   Otherwise, it will print the topological order and visualize the course prerequisite graph.

### Example:
If the following courses and prerequisites are provided:

```python
courses = ["Math", "Physics", "Programming", "Algorithms", "Databases", 
           "Linear Algebra", "Data Structures", "Operating Systems", 
           "AI", "Machine Learning"]

prerequisites = [
    ("Math", "Physics"), ("Math", "Algorithms"), ("Physics", "Programming"),
    ("Programming", "Databases"), ("Algorithms", "Data Structures"),
    ("Data Structures", "Operating Systems"), ("Operating Systems", "AI"),
    ("AI", "Machine Learning"), ("Linear Algebra", "AI"), ("Linear Algebra", "Machine Learning")
]
```

The script will output a valid order in which the courses should be taken. Additionally, a graph will be visualized to show the prerequisite structure (having graphviz is recommended so that it shows a more consistent graph).

# A* Pathfinding Game

This project is a simple **pathfinding application** that uses the A* algorithm to find the shortest path between two points on a grid. It is implemented in Python using the Pygame library for the graphical interface. 

## How to Use:
1. **Place the start and end nodes**: 
   - Left-click to place the **start node** (orange).
   - Left-click again to place the **end node** (turquoise).

2. **Draw obstacles**: 
   - Left-click and drag to place **obstacles** (black), which the algorithm will avoid.

3. **Run the algorithm**:
   - Press the **spacebar** to start the A* pathfinding algorithm.

4. **Reset the grid**:
   - Press **C** to clear the grid and start over.

## Color Legend:
- **Orange**: Start node
- **Turquoise**: End node
- **Green**: Nodes being explored
- **Red**: Processed nodes
- **Black**: Obstacles/barriers
- **Purple**: Final optimal path
- **White**: Empty/available spaces
- **Grey**: Grid lines

## Controls:
- **Left Mouse Button**: Place the start and end points, and draw obstacles.
- **Right Mouse Button**: Remove nodes or obstacles.
- **Spacebar**: Start the A* pathfinding algorithm.
- **C**: Clear the grid.

## Notes:
- **Heuristic**: The Manhattan distance is used to estimate the shortest distance between the current node and the end node.
