# Google Docs Structure for CS 554 Assignment 3

## Document Organization Guide

This outline helps you create a well-structured Google Docs document combining all deliverables and screenshots.

---

## **Task 1: Setting up an MCP Server** (24 PTS)

### Deliverable 1: Screenshot of Working Weather Server (12 pts)
- **Screenshot**: `screenshots/weather_alert_KY.png`
- **Content**: Insert screenshot showing:
  - Natural language query to Claude
  - Tool calls (get_alerts and/or get_forecast)
  - Formatted weather results
- **Text**: Copy from `Deliverables.md` Task 1, Deliverable 1 section

### Deliverable 2: Designing Your Own Tool (4 pts)
- **Text**: Copy from `Deliverables.md` Task 1, Deliverable 2 section
- **Content**: Steps to design a tool (stock prices, translations, movie info)

### Deliverable 3: Error Handling Importance (4 pts)
- **Text**: Copy from `Deliverables.md` Task 1, Deliverable 3 section
- **Content**: Why error handling is important for AI-connected tools

### Deliverable 4: Program-Consumable Output Format (4 pts)
- **Text**: Copy from `Deliverables.md` Task 1, Deliverable 4 section
- **Content**: How to change output design for program consumption

---

## **Task 2: Building Your First MCP Server** (31 PTS)

### Deliverable 1: Completed calc.py (20 pts)
- **Screenshots** (insert all):
  - `screenshots/differentiate_poly_expression.png`
  - `screenshots/integrate_expre.png`
  - `screenshots/solve_equation.png`
  - `screenshots/expectation_variance_bernoulli.png`
  - `screenshots/added_calculator_weather.png`
- **Text**: Copy from `Deliverables.md` Task 2, Deliverable 1 section
- **Note**: Include code file `calc.py` as attachment or link

### Deliverable 2: Symbolic vs Numeric Output Distinction (4 pts)
- **Text**: Copy from `Deliverables.md` Task 2, Deliverable 2 section

### Deliverable 3: Edge Cases and Error Handling (2 pts)
- **Text**: Copy from `Deliverables.md` Task 2, Deliverable 3 section

### Deliverable 4: Statistical Tool Implementation (5 pts)
- **Screenshot**: `screenshots/expectation_variance_bernoulli.png`
- **Text**: Copy from `Deliverables.md` Task 2, Deliverable 4 section

---

## **Task 3: Exploring Existing Ecosystem** (15 PTS)

### Deliverable 1: MCP Example Server Analysis (6 pts)
- **Text**: Copy from `Deliverables.md` Task 3, Deliverable 1 section
- **Content**: Description of selected server (Geolocation MCP Server)

### Deliverable 2: Claude Connectors Exploration (6 pts)
- **Text**: Copy from `Deliverables.md` Task 3, Deliverable 2 section
- **Content**: Available connectors and combination opportunities

### Deliverable 3: MCP Implementation Trade-offs (3 pts)
- **Text**: Copy from `Deliverables.md` Task 3, Deliverable 3 section
- **Content**: Trade-offs between formal MCP implementation and agent orchestration

---

## **Task 4: Model Distillation** (30 PTS + 5 EC)

### Part 1: Knowledge Distillation

#### Deliverable 1: Complete train_kd Function (12 pts)
- **Text**: Copy from `Deliverables.md` Task 4, Deliverable 1 section
- **Note**: Include code file `bert_dist.py` as attachment or link

#### Deliverable 2: Evaluation Results (4 pts)
- **Screenshot**: `screenshots/screenshot_bert_dist.png`
- **Text**: Copy from `Deliverables.md` Task 4, Deliverable 2 section
- **Content**: 
  - Fine-tune loss: 1.9622
  - Distillation loss: 2.8672
  - Evaluation metrics: exact_match=56.0, f1=57.6

#### Deliverable 3: Loss Function Explanation (2 pts)
- **Text**: Copy from `Deliverables.md` Task 4, Deliverable 3 section
- **Content**: How hard labels and soft teacher logits are combined

#### Deliverable 4: Benefits of Model Distillation (3 pts)
- **Text**: Copy from `Deliverables.md` Task 4, Deliverable 4 section

### Part 2: Agent Distillation

#### Deliverable 1: Teacher Agent Workflow (3 pts)
- **Text**: Copy from `Deliverables.md` Task 4.2, Deliverable 1 section

#### Deliverable 2: Distilled Student Learning (3 pts)
- **Text**: Copy from `Deliverables.md` Task 4.2, Deliverable 2 section

#### Deliverable 3: First-Thought Prefix Technique (3 pts)
- **Text**: Copy from `Deliverables.md` Task 4.2, Deliverable 3 section

#### Deliverable 4: Extra Credit - Running Distilled Agent (5 pts)
- **Screenshots** (insert both):
  - `screenshots/screenshot_quick_start_1.png`
  - `screenshots/screenshot_quick_start_2.png`
- **Text**: Copy from `Deliverables.md` Task 4.2, Deliverable 4 section
- **Content**: Observations on answer quality, speed/latency, and consistency

---

## Tips for Creating Google Docs

1. **Use Headings**: Use Google Docs heading styles (Heading 1 for Tasks, Heading 2 for Deliverables)
2. **Insert Screenshots**: Use Insert → Image → Upload from computer
3. **Formatting**: 
   - Use code blocks for code snippets (Format → Paragraph styles → Code)
   - Use bullet points for lists
   - Bold important terms
4. **Table of Contents**: Insert → Table of contents (auto-generated from headings)
5. **Page Breaks**: Insert page breaks between major tasks for better organization
6. **File Attachments**: For code files (calc.py, bert_dist.py), either:
   - Include as text in code blocks
   - Upload to Google Drive and link
   - Submit separately as required by assignment

---

## File Locations

- **Deliverables Text**: `/home/ujjwal/weather-mcp-server/Deliverables.md`
- **Screenshots**: `/home/ujjwal/weather-mcp-server/screenshots/`
- **Code Files**: 
  - `calc.py`
  - `bert_dist.py`
  - `weather.py`

---

## Checklist Before Submission

- [ ] All Task 1 deliverables with screenshots
- [ ] All Task 2 deliverables with screenshots and code
- [ ] All Task 3 deliverables (text only)
- [ ] All Task 4 Part 1 deliverables with screenshot
- [ ] All Task 4 Part 2 deliverables with screenshots
- [ ] Code files attached or linked
- [ ] Table of contents generated
- [ ] All screenshots clearly labeled and referenced
- [ ] Formatting consistent throughout
- [ ] Proofread for typos and clarity

