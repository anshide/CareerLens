import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState([]);
  const [skillGaps, setSkillGaps] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeResume = async () => {
    if (!file) return;

    setLoading(true);
    setError("");
    setResults([]);
    setSkillGaps([]);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/match",
        {
          method: "POST",
          body: formData,
        }
      );

      console.log("Response status:", response.status);

      if (!response.ok) {
        throw new Error(
          `Server returned ${response.status}`
        );
      }

      const data = await response.json();

      console.log("API response:", data);

      const matches = data.matches || [];

      setResults(matches);

      // -----------------------------------------
      // Calculate skill frequency
      // -----------------------------------------

      const skillFrequency = {};

      matches.forEach((job) => {
        job.missing_skills.forEach((skill) => {
          skillFrequency[skill] =
            (skillFrequency[skill] || 0) + 1;
        });
      });

      const gaps = Object.entries(skillFrequency)
        .map(([skill, count]) => ({
          skill,
          count,
          percentage:
            (count / matches.length) * 100,
        }))
        .sort((a, b) => b.count - a.count);

      setSkillGaps(gaps);

    } catch (error) {
      console.error("Match error:", error);

      setError(
        "Unable to analyze the resume. Make sure the backend is running."
      );
    } finally {
      setLoading(false);
    }
  };

  const resetAnalysis = () => {
    setFile(null);
    setResults([]);
    setSkillGaps([]);
    setError("");
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white">

      {/* ================= NAVBAR ================= */}

      <nav className="border-b border-slate-800">

        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-5">

          <h1 className="text-2xl font-bold">
            Career
            <span className="text-blue-500">
              Lens
            </span>
          </h1>

          <span className="text-sm text-slate-400">
            AI Career Matching
          </span>

        </div>

      </nav>


      {/* ================= MAIN ================= */}

      <main className="mx-auto max-w-5xl px-6 py-16">


        {/* ================= HERO ================= */}

        <section className="text-center">

          <h2 className="text-5xl font-bold leading-tight">

            Find jobs that match

            <span className="text-blue-500">
              {" "}your skills.
            </span>

          </h2>

          <p className="mx-auto mt-6 max-w-2xl text-lg text-slate-400">

            Upload your resume and CareerLens will
            analyze your skills, understand your experience,
            and find the most relevant jobs for you.

          </p>

        </section>


        {/* ================= UPLOAD ================= */}

        <section className="mx-auto mt-12 max-w-xl">

          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-8">

            <div className="rounded-xl border-2 border-dashed border-slate-700 p-10 text-center">


              {/* PDF ICON */}

              <div className="text-5xl">
                📄
              </div>


              <h3 className="mt-4 text-xl font-semibold">
                Upload your resume
              </h3>


              <p className="mt-2 text-sm text-slate-400">
                Upload a PDF resume
              </p>


              {/* FILE INPUT */}

              <label className="mt-6 inline-block cursor-pointer rounded-lg bg-blue-600 px-6 py-3 font-medium transition hover:bg-blue-500">

                Choose Resume

                <input
                  type="file"
                  accept=".pdf,application/pdf"
                  className="hidden"
                  onChange={(event) => {

                    const selectedFile =
                      event.target.files[0];

                    if (
                      selectedFile &&
                      selectedFile.type ===
                        "application/pdf"
                    ) {
                      setFile(selectedFile);
                      setError("");
                    } else {
                      setError(
                        "Please select a PDF file."
                      );
                    }

                  }}
                />

              </label>


              {/* SELECTED FILE */}

              {file && (

                <div className="mt-5 rounded-lg bg-slate-800 px-4 py-3">

                  <p className="text-sm text-green-400">
                    ✓ {file.name}
                  </p>

                </div>

              )}

            </div>


            {/* ANALYZE BUTTON */}

            <button
              disabled={!file || loading}
              onClick={analyzeResume}
              className="mt-6 w-full rounded-lg bg-blue-600 py-3 font-semibold transition hover:bg-blue-500 disabled:cursor-not-allowed disabled:opacity-40"
            >

              {loading
                ? "Analyzing Resume..."
                : "Analyze Resume"}

            </button>


            {/* ERROR */}

            {error && (

              <div className="mt-4 rounded-lg border border-red-500/30 bg-red-500/10 p-3 text-center text-sm text-red-400">

                {error}

              </div>

            )}

          </div>

        </section>


        {/* ================= LOADING ================= */}

        {loading && (

          <div className="mt-12 text-center">

            <div className="text-lg font-medium">
              Analyzing your resume...
            </div>

            <p className="mt-2 text-sm text-slate-500">
              Extracting skills and comparing jobs
            </p>

          </div>

        )}


        {/* ================= SKILL GAP ================= */}

        {!loading && skillGaps.length > 0 && (

          <section className="mt-16">

            <div className="rounded-2xl border border-slate-800 bg-slate-900 p-7">

              <h2 className="text-2xl font-bold">
                Skill Gap Analysis
              </h2>

              <p className="mt-2 text-slate-400">
                Skills that are missing from your resume
                but appear in your recommended jobs.
              </p>


              <div className="mt-6 space-y-3">

                {skillGaps.map((item) => (

                  <div
                    key={item.skill}
                    className="flex items-center justify-between rounded-lg bg-slate-800 px-4 py-3"
                  >

                    <span className="font-medium">
                      {item.skill}
                    </span>

                    <span className="text-sm text-red-400">
                      {item.percentage.toFixed(0)}% of jobs
                    </span>

                  </div>

                ))}

              </div>

            </div>

          </section>

        )}


        {/* ================= JOB RESULTS ================= */}

        {!loading && results.length > 0 && (

          <section className="mt-16">

            <div className="flex items-center justify-between">

              <div>

                <h2 className="text-3xl font-bold">
                  Your Top Job Matches
                </h2>

                <p className="mt-2 text-slate-400">
                  Jobs ranked according to your resume.
                </p>

              </div>


              <button
                onClick={resetAnalysis}
                className="rounded-lg border border-slate-700 px-4 py-2 text-sm text-slate-300 transition hover:bg-slate-800"
              >
                New Resume
              </button>

            </div>


            {/* JOB CARDS */}

            <div className="mt-8 space-y-5">

              {results.map((job, index) => (

                <div
                  key={job.job_id}
                  className="rounded-2xl border border-slate-800 bg-slate-900 p-6 transition hover:border-slate-700"
                >


                  {/* HEADER */}

                  <div className="flex items-start justify-between gap-6">

                    <div>

                      <p className="text-sm text-slate-500">
                        #{index + 1}
                      </p>

                      <h3 className="mt-1 text-xl font-semibold">
                        {job.title}
                      </h3>

                      <p className="mt-1 text-slate-400">
                        {job.company}
                      </p>

                    </div>


                    {/* FINAL SCORE */}

                    <div className="text-right">

                      <p className="text-3xl font-bold text-blue-500">

                        {(job.final_score * 100).toFixed(0)}%

                      </p>

                      <p className="text-xs text-slate-500">
                        Match Score
                      </p>

                    </div>

                  </div>


                  {/* SCORE BREAKDOWN */}

                  <div className="mt-6 grid grid-cols-2 gap-4">

                    <div className="rounded-lg bg-slate-800 p-4">

                      <p className="text-sm text-slate-400">
                        Semantic Match
                      </p>

                      <p className="mt-1 text-xl font-semibold">

                        {(job.semantic_score * 100).toFixed(0)}%

                      </p>

                    </div>


                    <div className="rounded-lg bg-slate-800 p-4">

                      <p className="text-sm text-slate-400">
                        Skill Match
                      </p>

                      <p className="mt-1 text-xl font-semibold">

                        {(job.skill_score * 100).toFixed(0)}%

                      </p>

                    </div>

                  </div>


                  {/* MATCHED SKILLS */}

                  {job.matched_skills.length > 0 && (

                    <div className="mt-6">

                      <p className="mb-3 text-sm font-medium text-slate-300">
                        Matched Skills
                      </p>

                      <div className="flex flex-wrap gap-2">

                        {job.matched_skills.map(
                          (skill) => (

                            <span
                              key={skill}
                              className="rounded-full bg-green-500/10 px-3 py-1 text-sm text-green-400"
                            >
                              ✓ {skill}
                            </span>

                          )
                        )}

                      </div>

                    </div>

                  )}


                  {/* MISSING SKILLS */}

                  {job.missing_skills.length > 0 && (

                    <div className="mt-5">

                      <p className="mb-3 text-sm font-medium text-slate-300">
                        Skill Gaps
                      </p>

                      <div className="flex flex-wrap gap-2">

                        {job.missing_skills.map(
                          (skill) => (

                            <span
                              key={skill}
                              className="rounded-full bg-red-500/10 px-3 py-1 text-sm text-red-400"
                            >
                              + {skill}
                            </span>

                          )
                        )}

                      </div>

                    </div>

                  )}

                </div>

              ))}

            </div>

          </section>

        )}


        {/* ================= EMPTY STATE ================= */}

        {!loading &&
          results.length === 0 &&
          !error && (

            <div className="mt-16 text-center text-slate-500">

              Upload your resume to discover
              matching jobs.

            </div>

          )}

      </main>


      {/* ================= FOOTER ================= */}

      <footer className="border-t border-slate-800 py-8 text-center text-sm text-slate-500">

        CareerLens — AI-powered career matching

      </footer>

    </div>
  );
}

export default App; 