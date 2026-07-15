# Topics

Comprehensive learning resources organized by subject. Each subject contains topics progressing from beginner to research level, with visual diagrams (Mermaid), mathematical notation (MathJax), and source references (Wikipedia, arXiv, textbooks).

## Meta Topics (By Subject)

### Mathematics
- [**Mathematics Hub**](Math/index.html) - Comprehensive guide to mathematical foundations and theory

  **Topics:** Algebraic Operations, Set Theory, Mathematical Logic, Functions, Equations & Inequalities, Geometry, Calculus, Linear Algebra, Numerical Methods & Analysis, Real Analysis

---

## How to Navigate

1. **Select a subject** from the list above
2. **Click the hub** to see all topics in that subject
3. **Choose a topic** and select your learning level:
   - **Beginner** - Start here for foundational understanding
   - **Intermediate** - Build skills and applications
   - **Advanced** - Theoretical depth and specialization
   - **Research** - Cutting-edge topics and open problems

## Adding New Topics

See [TEMPLATE.html](TEMPLATE.html), [COMPONENTS.md](COMPONENTS.md), and [new-topic.py](new-topic.py) in the topics directory.

```bash
# Create a new topic (automated)
cd topics
python3 new-topic.py <TOPIC_FOLDER> "Your Topic Name"

# Or manual: copy template and edit
cp TEMPLATE.html <TOPIC_FOLDER>/YourTopic.html
```