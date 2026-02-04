
def generate_subquestions(query):
    return [query]

def clean_subquestions(subqs):
    return [q for q in subqs if len(q) > 5]
