from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS = [
    "python","java","c++","sql","html","css","javascript",
    "react","node","flask","django","machine learning",
    "data analysis","excel","communication","teamwork"
]

def extract_skills(text):
    text = text.lower()
    return [s for s in SKILLS if s in text]

def analyze_resumes(resumes, jd, names):
    jd_skills = extract_skills(jd)

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(resumes + [jd])
    sim_scores = cosine_similarity(tfidf[-1], tfidf[:-1])[0]

    results = []

    for i, resume in enumerate(resumes):
        res_skills = extract_skills(resume)

        matched = list(set(res_skills) & set(jd_skills))
        missing = list(set(jd_skills) - set(res_skills))

        skill_score = len(matched)/(len(jd_skills)+1) * 100
        sim_score = sim_scores[i] * 100

        final_score = round((0.6*skill_score + 0.4*sim_score),2)

        # 🔥 WHY explanation
        reason = f"Matched {len(matched)} skills, Missing {len(missing)} skills"

        # 🔥 Suggestions
        suggestions = missing[:5]

        results.append({
            "name": names[i],
            "score": final_score,
            "matched": matched,
            "missing": missing,
            "reason": reason,
            "suggestions": suggestions
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    for i, r in enumerate(results):
        r["rank"] = i+1

    return results