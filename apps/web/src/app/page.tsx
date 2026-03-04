export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-zinc-950 text-white">
      <main className="flex flex-col items-center gap-8 px-6 text-center">
        {/* 8-bit Moxling placeholder */}
        <div className="text-8xl" role="img" aria-label="Moxling egg">
          <pre className="font-mono text-4xl leading-tight text-purple-400">
{`    ████
  ██░░░░██
 █░░░░░░░░█
 █░░▓░░▓░░█
 █░░░░░░░░█
 █░░░▼░░░░█
  ██░░░░██
    ████`}
          </pre>
        </div>

        <h1 className="text-5xl font-bold tracking-tight">
          <span className="text-purple-400">Moxling</span> Pets
        </h1>

        <p className="max-w-md text-lg text-zinc-400">
          Your AI Tamagotchi. A digital creature that reflects your values,
          grows with you, and acts in the world on your behalf.
        </p>

        <div className="flex flex-col gap-3 sm:flex-row">
          <button className="rounded-full bg-purple-600 px-8 py-3 font-semibold transition-colors hover:bg-purple-500">
            Hatch Your Moxling
          </button>
          <a
            href="https://github.com/xia16/moxling-pets"
            className="rounded-full border border-zinc-700 px-8 py-3 font-semibold transition-colors hover:border-zinc-500"
          >
            GitHub
          </a>
        </div>

        <div className="mt-12 grid max-w-2xl grid-cols-1 gap-6 text-left sm:grid-cols-2">
          {[
            {
              title: "Safe by Default",
              desc: "Guardrails are baked in. Your Moxling can't accidentally spend $450K.",
            },
            {
              title: "Reflective Identity",
              desc: "Its personality and 8-bit appearance evolve to mirror who you are.",
            },
            {
              title: "SOUL.md",
              desc: "A living identity document that persists across sessions. No more lost context.",
            },
            {
              title: "Real-World Agency",
              desc: "Browse, search, message, find dates — all within guardrails you gradually unlock.",
            },
          ].map((feature) => (
            <div
              key={feature.title}
              className="rounded-xl border border-zinc-800 p-5"
            >
              <h3 className="mb-2 font-semibold text-purple-400">
                {feature.title}
              </h3>
              <p className="text-sm text-zinc-400">{feature.desc}</p>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}
