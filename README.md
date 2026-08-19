<h1 align="center">Ross Farrell</h1>

<p align="center">
  <strong>Data Architect · Systems Engineer · Software Developer</strong><br />
  Perth, Western Australia
</p>

<p align="center">
  <a href="https://hypecoding.dev">Portfolio</a> ·
  <a href="https://duckdive.gold">DuckDive</a> ·
  <a href="https://perthhousedata.com">Perth House Data</a> ·
  <a href="https://linkedin.com/in/rossfarrellvirtualengineer">LinkedIn</a>
</p>

---

I design systems for problems that are usually messier than the diagram suggests.

My background spans software development, data architecture, automation and modern application platforms. Most of my work sits somewhere between those boundaries: taking awkward source systems, ambiguous business rules, unreliable interfaces or emerging technology and turning them into something **observable, explainable and useful**.

I am most interested in the full path from source to decision:

**data → contracts → transformation → orchestration → interface → human or agent action**

The implementation may be SQL, PySpark, TypeScript, React, Power BI, Microsoft Fabric, Azure, Postgres, DuckDB/MotherDuck or something else entirely. I am less attached to the tool than to whether the resulting system can be understood, tested and operated safely.

## DuckDive

[**DuckDive**](https://duckdive.gold) started as an experiment in agentic BI.

I wanted a way to demonstrate how an agent could investigate real data without exposing company information, pre-building a semantic model, or quietly giving the model the answer in advance.

The basic idea is deliberately small:

> Give each user a bounded analytical environment, a robust data contract and an agent with enough authority to explore the data, build useful analytical components, and reject questions the available evidence cannot support.

That experiment became more interesting than the original demo.

While investigating vehicle-market data, the agent independently built a **Price Frontier**: a Pareto-style view of listings that were simultaneously better on price, age and mileage. It then applied the same reasoning at both the whole-market and make/model level.

That raised a much more useful architectural question than “can an LLM make a dashboard?”

**How much traditional BI infrastructure is still necessary when the consumer of the analytical layer is an agent rather than a human?**

`Next.js` · `TypeScript` · `MotherDuck` · `DuckDB` · `Agent tooling` · `Bounded execution` · `Generated analytical views`

**[Open DuckDive →](https://duckdive.gold)** · **[Read the source →](https://github.com/Big-jpg/duckdive)**

## Perth House Data

[**Perth House Data**](https://perthhousedata.com) is a free public analytical product built from roughly three decades of Perth house-sale records.

The interesting part is not the dashboard. It is the data path required to make a fragmented historical dataset trustworthy enough that ordinary people can inspect it themselves.

| | |
|---|---|
| **Coverage** | 30 years · 330 suburbs · 281k+ recorded house sales |
| **Data path** | Source CSV → immutable raw archive → canonical property model → cleaned facts → analytical curation |
| **Platform** | Next.js · Vercel Workflows and Blob · Neon Postgres · MotherDuck |
| **Analysis** | Rolling medians · annual movement · sales velocity · land/value relationships · bedroom cohorts |
| **Output** | Public suburb explorer · downloadable CSV · reusable analytical views |

The source remains available because an analytical product should not require users to trust the interface more than the evidence underneath it.

**[Explore the live product →](https://perthhousedata.com)** · **[Read the source →](https://github.com/Big-jpg/real-data-for-all)**

## Selected systems

### ModelViz

[**ModelViz**](https://github.com/Big-jpg/modelviz) is a browser-based architecture tool for inspecting Power BI and Microsoft Fabric semantic models: tables, relationships, storage modes, dependencies and row-level security.

It exists because complex semantic models are much easier to reason about when their actual structure is visible.

`Next.js` · `TypeScript` · `TMDL parsing` · `Interactive architecture diagrams` · `Security inspection`

**[Open ModelViz →](https://modelviz-alpha.vercel.app)**

### Fabric Semantic Model Starter

[**Fabric Semantic Model Starter**](https://github.com/Big-jpg/fabric-apps-react-webapp-starter) is a React and TypeScript foundation for Microsoft Fabric Apps.

Rather than treating the semantic model as something that only Power BI understands, it reads live DAX metadata and turns the model into an explorable application surface.

`React 19` · `TypeScript` · `Microsoft Fabric Apps` · `DAX metadata` · `Config-driven deployment`

### GitHub Motion Graph

[**GitHub Motion Graph**](https://github.com/Big-jpg/github-motion-graph) turns repositories, commits, branches and pull requests into a force-directed visual system.

It is partly a visualisation experiment and partly an attempt to make software activity itself easier to inspect as a changing system rather than a list of events.

`Next.js 16` · `React Server Components` · `Edge and Node APIs` · `Neon Postgres` · `Drizzle ORM` · `Vercel`

## How I tend to build

I usually start by asking whether the problem is actually where everyone thinks it is.

A reporting problem may be a source-system problem. A performance problem may be an orchestration problem. A governance problem may really be an identity problem. A request for another abstraction layer may disappear once the contract underneath it becomes explicit.

From there, my preferred systems are:

- **Observable** — failures and state transitions should be visible.
- **Governed** — authority, identity and scope should be explicit.
- **Replayable** — important work should be reproducible rather than dependent on hidden state.
- **Explainable** — another human should be able to work out why the system produced what it did.

I like automation, but not for its own sake. If removing a constraint or making one small schema change eliminates an entire workflow, that is usually the better architecture.

## Research and experiments

- [**Convergent**](https://github.com/Big-jpg/convergent) — Multi-agent reasoning, coordination and emergent system behaviour.
- [**OrbitMe**](https://github.com/Big-jpg/orbitme) — A Newtonian orbital simulator for spatial computing, inspired by *The Expanse*.
- [**next-boids-text**](https://github.com/Big-jpg/next-boids-text) — Generative typography driven by flocking behaviour and real-time interaction.
- [**Pixel-to-Voxel Projector**](https://github.com/Big-jpg/Pixeltovoxelprojector) — Experimental image-to-spatial reconstruction.
- [**Recupare**](https://github.com/Big-jpg/recupare) — Secure invoice intelligence using Azure Content Understanding, isolated user data and structured extraction workflows.

A lot of these projects begin the same way: **I wonder if this is actually necessary.**

Sometimes the answer is yes. Occasionally that turns into something much more interesting.

## Tools I reach for

**Data and analytics**  
Microsoft Fabric · OneLake · Delta · Power BI · SQL · PySpark · DuckDB · MotherDuck · Postgres

**Software and platforms**  
TypeScript · Python · React · Next.js · Azure · Vercel · APIs · identity · distributed systems

**Automation and agents**  
Metadata-driven orchestration · event-driven workflows · bounded agent contracts · tool calling · observability · human-in-the-loop controls

## Contact

If you are working on a difficult data platform, an automation problem that has outgrown the process around it, or an experiment where the architecture matters as much as the demo, feel free to get in touch.

**[hypecoding.dev](https://hypecoding.dev)** · **[LinkedIn](https://linkedin.com/in/rossfarrellvirtualengineer)** · **[rossfarrell7@gmail.com](mailto:rossfarrell7@gmail.com)**

---

<p align="center">
  Build the smallest system that makes the difficult thing dependable.
</p>
