# Min-Cost Max-Flow Problem Solver 🚀

This repository contains a **Linear Programming (LP) solver** designed to solve the **Min-Cost Max-Flow (MCMF) problem**. With the help of the **PuLP library**, this solver efficiently models and solves the optimization problem, ensuring a clear and simple interface for users. 🎯

---

## 🔍 What is the Min-Cost Max-Flow Problem?

The **Min-Cost Max-Flow problem** is a fundamental optimization problem in graph theory. It involves finding the maximum possible flow between a source and a destination in a network, while minimizing the total cost of the flow.

This problem arises in various real-world applications such as:

- Transportation and logistics planning
- Network routing
- Supply chain optimization

The goal is to optimize the flow through a graph's edges while respecting constraints like capacity and cost.

---

## 📋 Input Format

Your input data must be written in the `input.txt` file. The format should be as follows:

1. **Vertices, Edges, The Source, and Sink**: Define the number of vertices, edges, the source, and sink in the graph on the first line.
2. **Source and Destination**: Specify the source vertex, destination vertex, and corresponding capacity and cost for each edge.

### Example Input

```plaintext
5 7 0 4
0 1 10 5
0 2 15 8
1 3 10 2
2 3 10 1
1 4 15 3
3 4 10 2
0 4 20 7
```

Here:

- `5 7 0 4` indicates 5 vertices, 7 edges, the source is vertex 0 and the sink is vertex 4.
- Each subsequent line defines an edge with:
  - Source vertex
  - Destination vertex
  - Capacity
  - Cost per unit flow

---

## 🔧 Technologies Used

This project is implemented in Python using the **PuLP** library.

### 📘 About PuLP

[PuLP](https://pypi.org/project/PuLP/) is a Python library for modeling and solving Linear Programming (LP) and Integer Programming (IP) problems. It provides:

- An easy-to-use interface to define LP variables, constraints, and objectives.
- Compatibility with several solvers such as CBC (default), Gurobi, and CPLEX.
- Comprehensive support for both small-scale and large-scale optimization problems.

---

## 🏃‍♂️ How to Run the Solver?

To solve the Min-Cost Max-Flow problem, simply run the `LP.py` file after preparing your input data in `input.txt`:

```bash
python LP.py
```

The output will display the optimal flow and cost for the given network. 🎉

---

## 🤝 Contributing

If you encounter any issues, bugs, or have suggestions, I’d love to hear from you! Feel free to open an issue or submit a pull request. Your feedback helps make this project better! 🙌

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

### 🌟 Thank You for Visiting!

If you find this project helpful, don’t forget to give it a ⭐️ on GitHub! Your support means the world. 🌍
