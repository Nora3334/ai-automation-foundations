# Architecture Overview

This project implements an end-to-end AI automation pipeline:

1. CSV lead data ingestion
2. Pre-processing into structured Python dictionaries
3. Real-time AI classification using OpenAI API
4. Post-processing into JSON and CSV outputs

The system is modular to allow:
- Easy model replacement
- API integration
- Scaling into web or agent-based workflows
