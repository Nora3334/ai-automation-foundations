# How This Automation Works (Plain English)

This automation is designed for non-technical users and business owners.

## Step 1: Lead Capture
Leads are added to a Google Sheet from any source (website forms, manual entry, integrations).

## Step 2: Trigger
Make watches the spreadsheet for new rows and automatically starts the workflow.

## Step 3: AI Classification
Each lead is sent to OpenAI with a structured prompt asking the model to evaluate lead quality.

## Step 4: Parsing
The AI response is returned as JSON and parsed so individual fields can be used.

## Step 5: Output
The original Google Sheet row is updated with:
- Lead Score
- AI Reasoning

## Result
Sales teams instantly see which leads require immediate attention, without manual review.

---

## Why No-Code Was Used
- Faster delivery than custom code
- Easy for clients to understand and maintain
- Ideal for SMB automation and consulting use cases

---

## Limitations
- Dependent on OpenAI availability
- Requires well-structured prompts
- Best suited for small-to-medium lead volumes

---

## When to Use This Approach
- Rapid MVPs
- Client projects
- Internal business automation
- Non-technical stakeholders
