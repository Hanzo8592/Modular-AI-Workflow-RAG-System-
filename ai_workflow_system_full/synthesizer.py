
def synthesize_answer(query, evidence_chunks):
    if not evidence_chunks:
        return "Insufficient evidence found."
    return f"Synthesized answer for: {query}\nUsing {len(evidence_chunks)} evidence chunks."
