import os
import base64
import subprocess

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

def generate_report():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    screenshots_dir = os.path.join(base_dir, "screenshots")
    
    img_login = get_base64_image(os.path.join(screenshots_dir, "login_screen.png"))
    img_browse = get_base64_image(os.path.join(screenshots_dir, "browse_donations.png"))
    img_donor = get_base64_image(os.path.join(screenshots_dir, "donor_dashboard.png"))
    img_admin = get_base64_image(os.path.join(screenshots_dir, "admin_analytics.png"))
    img_cert = get_base64_image(os.path.join(screenshots_dir, "volunteer_certificate.png"))

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>FoodRescue Technical Project Report - CSE 494</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

    @page {{
      size: A4 portrait;
      margin: 0;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      color: #1e293b;
      background: #e2e8f0;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}

    .page {{
      width: 210mm;
      height: 297mm;
      margin: 20px auto;
      padding: 22mm 24mm 20mm 24mm;
      background: #ffffff;
      position: relative;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
      page-break-after: always;
      break-after: page;
    }}

    @media print {{
      body {{
        background: transparent;
      }}
      .page {{
        margin: 0;
        box-shadow: none;
        width: 210mm;
        height: 297mm;
      }}
    }}

    /* Running Header & Footer */
    .running-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #cbd5e1;
      padding-bottom: 6px;
      margin-bottom: 18px;
      font-size: 8.5pt;
      font-weight: 700;
      color: #64748b;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }}

    .running-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid #e2e8f0;
      padding-top: 6px;
      font-size: 8pt;
      color: #64748b;
    }}

    .page-content {{
      flex: 1;
      display: flex;
      flex-direction: column;
    }}

    /* Typography */
    h1.main-title {{
      font-size: 32pt;
      font-weight: 900;
      color: #1e3a8a;
      letter-spacing: 0.05em;
      text-align: center;
      margin-bottom: 8px;
    }}

    .subtitle {{
      font-size: 11pt;
      font-weight: 700;
      color: #1e293b;
      text-align: center;
      margin-bottom: 4px;
    }}

    .sub-tag {{
      font-size: 9pt;
      color: #64748b;
      text-align: center;
      margin-bottom: 30px;
    }}

    .report-badge {{
      text-align: center;
      font-size: 9pt;
      font-weight: 800;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #334155;
      margin-bottom: 35px;
    }}

    h2.section-heading {{
      font-size: 11.5pt;
      font-weight: 800;
      color: #0f172a;
      margin-top: 14px;
      margin-bottom: 8px;
      letter-spacing: -0.01em;
    }}

    h3.subsection-heading {{
      font-size: 9.5pt;
      font-weight: 700;
      color: #1e293b;
      margin-top: 10px;
      margin-bottom: 4px;
    }}

    p {{
      font-size: 8.8pt;
      line-height: 1.52;
      color: #334155;
      margin-bottom: 8px;
      text-align: justify;
    }}

    ul, ol {{
      margin-left: 18px;
      margin-bottom: 8px;
    }}

    li {{
      font-size: 8.6pt;
      line-height: 1.48;
      color: #334155;
      margin-bottom: 3px;
    }}

    /* Tables */
    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0 12px;
      font-size: 8.4pt;
    }}

    table.data-table th, table.data-table td {{
      border: 1px solid #cbd5e1;
      padding: 5px 8px;
      text-align: left;
    }}

    table.data-table th {{
      background-color: #1e3a8a;
      color: #ffffff;
      font-weight: 700;
      font-size: 8.5pt;
    }}

    table.data-table tr:nth-child(even) td {{
      background-color: #f8fafc;
    }}

    /* Code Blocks */
    .code-box {{
      background: #0f172a;
      color: #f8fafc;
      padding: 6px 10px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.8pt;
      line-height: 1.35;
      margin: 5px 0 8px;
      overflow: hidden;
      white-space: pre-wrap;
      word-break: break-all;
    }}

    code.inline-code {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 8pt;
      background: #f1f5f9;
      color: #0f766e;
      padding: 1px 4px;
      border-radius: 3px;
      border: 1px solid #e2e8f0;
    }}

    /* Figures & Screenshots */
    .figure-container {{
      margin: 8px 0 10px;
      text-align: center;
    }}

    .figure-img {{
      max-width: 100%;
      height: auto;
      max-height: 180px;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
      display: block;
      margin: 0 auto;
    }}

    .figure-caption {{
      font-size: 7.8pt;
      font-weight: 700;
      color: #475569;
      margin-top: 4px;
      text-align: center;
    }}

    /* Cover Page Specific Styles */
    .cover-top-label {{
      text-align: center;
      font-size: 8.5pt;
      font-weight: 700;
      letter-spacing: 0.22em;
      color: #475569;
      text-transform: uppercase;
      margin-top: 30mm;
      margin-bottom: 25mm;
    }}

    .meta-card {{
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 16px 22px;
      width: 250px;
      margin: 0 auto 30mm;
      background: #ffffff;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
    }}

    .meta-row {{
      display: flex;
      justify-content: space-between;
      font-size: 9pt;
      line-height: 1.9;
    }}

    .meta-label {{
      font-weight: 700;
      color: #1e293b;
    }}

    .meta-val {{
      color: #334155;
    }}

    .course-block {{
      text-align: center;
      margin-bottom: 20mm;
    }}

    .course-title {{
      font-size: 16pt;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 4px;
    }}

    .course-sub {{
      font-size: 10pt;
      color: #475569;
      font-weight: 500;
    }}

    .date-label {{
      text-align: center;
      font-size: 9pt;
      color: #64748b;
      margin-bottom: 10mm;
    }}

    /* High Level Arch Diagram */
    .arch-diagram {{
      display: flex;
      justify-content: space-between;
      gap: 10px;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 12px;
      margin: 8px 0 12px;
    }}

    .arch-box {{
      flex: 1;
      background: #0f172a;
      color: white;
      border-radius: 4px;
      padding: 8px 10px;
      font-size: 7.5pt;
      text-align: center;
    }}

    .arch-box.client {{
      background: #0369a1;
    }}

    .arch-box.backend {{
      background: #1e1b4b;
    }}

    .arch-box.database {{
      background: #064e3b;
    }}

    .arch-box h4 {{
      font-size: 8.2pt;
      font-weight: 700;
      margin-bottom: 4px;
      color: #ffffff;
      border-bottom: 1px solid rgba(255,255,255,0.2);
      padding-bottom: 2px;
    }}

    .arch-box ul {{
      list-style: none;
      margin-left: 0;
      text-align: left;
    }}

    .arch-box li {{
      color: #e2e8f0;
      font-size: 7pt;
      margin-bottom: 2px;
    }}
  </style>
</head>
<body>

  <!-- =========================================================================
       PAGE 1: TITLE COVER PAGE (EXACT STRUCTURE AS ATTACHED PDF)
  ========================================================================== -->
  <div class="page">
    <div class="cover-top-label">
      FOODRESCUE &bull; TECHNICAL PROJECT REPORT
    </div>

    <div style="text-align: center; margin-bottom: 20mm;">
      <h1 class="main-title">FOODRESCUE</h1>
      <div class="subtitle">Intelligent Food Waste Rescue & Redistribution System</div>
      <div class="sub-tag">(Powered by PyMongo & MongoDB 8.x)</div>
      <div class="report-badge">TECHNICAL PROJECT REPORT</div>
    </div>

    <div class="meta-card">
      <div class="meta-row">
        <span class="meta-label">Submitted by:</span>
        <span class="meta-val">Manikanta Bandi</span>
      </div>
      <div class="meta-row">
        <span class="meta-label">Roll No:</span>
        <span class="meta-val">46</span>
      </div>
      <div class="meta-row">
        <span class="meta-label">Registration No:</span>
        <span class="meta-val">12308271</span>
      </div>
    </div>

    <div class="course-block">
      <div class="course-title">CSE 494</div>
      <div class="course-sub">Intelligent NoSQL Databases</div>
    </div>

    <div class="date-label">
      Submission date: 29 &ndash; 10 &ndash; 2026
    </div>

    <div class="running-footer">
      <span>FoodRescue Technical Project Report</span>
      <span>Page 1</span>
    </div>
  </div>


  <!-- =========================================================================
       PAGE 2: INTRODUCTION & TECHNOLOGY STACK (EXACT MATCH TO PAGE 2)
  ========================================================================== -->
  <div class="page">
    <div>
      <div class="running-header">
        <span>FOODRESCUE | TECHNICAL PROJECT REPORT</span>
        <span>CSE 494 - INTELLIGENT NOSQL DATABASES</span>
      </div>

      <div class="page-content">
        <h2 class="section-heading">1. Introduction</h2>
        <p>
          FoodRescue is a web-based food waste rescue and redistribution platform designed to connect commercial food donors, certified charitable shelters, and volunteer couriers using MongoDB. In metropolitan centers, commercial kitchens discard tons of edible surplus food daily while community pantries experience food deficits. FoodRescue establishes database-level constraints and high-throughput queries to coordinate the complete surplus food lifecycle.
        </p>
        <p>
          FoodRescue brings surplus food listing, sequential tracking, administrative verification queues, multi-factor JWT authentication, digital courier dispatch, and multi-stage aggregation analytics into one seamless interface. It is engineered to enforce statutory food safety and allocation rules directly at the MongoDB database engine layer.
        </p>

        <h3 class="subsection-heading">1.1 Problem Statement</h3>
        <p>
          Institutions need a reliable way to coordinate surplus food redistribution without risking double-claims, delivery failure, or shelf-life expiration, while ensuring sub-millisecond query verification and transparent distribution metrics.
        </p>

        <h3 class="subsection-heading">1.2 Objectives</h3>
        <ul>
          <li>Provide a browser-based workspace for food donation, shelter claims, and courier dispatch.</li>
          <li>Enforce MongoDB <code class="inline-code">$jsonSchema</code> rules to reject negative quantities (Quantity &le; 0) and malformed records.</li>
          <li>Prevent duplicate claiming using atomic state operations (<code class="inline-code">find_one_and_update</code>) and Compound Indexes.</li>
          <li>Implement role-based JWT authentication and 1-click evaluator demo logins.</li>
          <li>Execute multi-stage aggregation pipelines for real-time rescued volume, donor impact, and certified leaderboards.</li>
        </ul>

        <h2 class="section-heading">2. Technology Stack</h2>
        <table class="data-table">
          <thead>
            <tr>
              <th style="width: 30%;">Technology</th>
              <th style="width: 70%;">Purpose</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Python 3.11+</strong></td>
              <td>Backend application logic, cryptographic hashing, and REST API services.</td>
            </tr>
            <tr>
              <td><strong>PyMongo 4.x</strong></td>
              <td>Native MongoDB driver providing BSON serialization and connection pooling.</td>
            </tr>
            <tr>
              <td><strong>MongoDB Community 8.x</strong></td>
              <td>Document database hosting indexed collections with engine-level <code class="inline-code">$jsonSchema</code>.</td>
            </tr>
            <tr>
              <td><strong>Flask Microframework</strong></td>
              <td>HTTP routing, JWT-based access control, and JSON API microservices.</td>
            </tr>
            <tr>
              <td><strong>React 18 & Vite</strong></td>
              <td>Reactive component-based user interface with rapid HMR and optimized builds.</td>
            </tr>
            <tr>
              <td><strong>Tailwind CSS</strong></td>
              <td>Custom responsive interface with clean aesthetics and split-screen sliding layouts.</td>
            </tr>
            <tr>
              <td><strong>Recharts</strong></td>
              <td>Interactive client-side visualizations for rescued food velocity and category breakdowns.</td>
            </tr>
          </tbody>
        </table>

        <h3 class="subsection-heading">2.1 High-Level Architecture</h3>
        <p>
          The frontend communicates with Flask endpoints over JSON. Flask handles session tokens and dispatches database operations through PyMongo. MongoDB enforces validation schemas on write and maintains compound unique indexes. Verified delivery receipts update volunteer impact telemetry directly in the database.
        </p>
      </div>
    </div>

    <div class="running-footer">
      <span>FoodRescue Technical Project Report</span>
      <span>Page 2</span>
    </div>
  </div>


  <!-- =========================================================================
       PAGE 3: ARCHITECTURE & MAIN FEATURES (EXACT MATCH TO PAGE 3)
  ========================================================================== -->
  <div class="page">
    <div>
      <div class="running-header">
        <span>FOODRESCUE | TECHNICAL PROJECT REPORT</span>
        <span>CSE 494 - INTELLIGENT NOSQL DATABASES</span>
      </div>

      <div class="page-content">
        <div class="figure-caption" style="margin-bottom: 6px; font-size: 8.5pt;">Figure 1. FoodRescue System Architecture</div>
        
        <div class="arch-diagram">
          <div class="arch-box client">
            <h4>Client Frontend (React 18)</h4>
            <ul>
              <li>&bull; Donor Food Listing Portal</li>
              <li>&bull; NGO Atomic Claim Interface</li>
              <li>&bull; Volunteer Courier Hub</li>
              <li>&bull; Admin Analytics (Recharts)</li>
              <li>&bull; Sliding Split-Screen Auth UI</li>
            </ul>
          </div>

          <div class="arch-box backend">
            <h4>Flask REST Backend</h4>
            <ul>
              <li>&bull; JWT RBAC Gatekeeper</li>
              <li>&bull; Atomic Claim Coordinator</li>
              <li>&bull; Idempotent Points Engine</li>
              <li>&bull; 6 Multi-Stage Aggregations</li>
              <li>&bull; PyMongo 4.x Connection Pool</li>
            </ul>
          </div>

          <div class="arch-box database">
            <h4>MongoDB 8.x Engine</h4>
            <ul>
              <li>&bull; foodrescue_db</li>
              <li>&bull; donations (Schema: quantity &gt; 0)</li>
              <li>&bull; delivery_tasks (Atomic locking)</li>
              <li>&bull; volunteer_profiles (Leaderboard)</li>
              <li>&bull; Native $jsonSchema Engine</li>
            </ul>
          </div>
        </div>

        <h2 class="section-heading">3. Main Features and Implementation</h2>

        <h3 class="subsection-heading">3.1 Sliding Split-Screen Authentication UI</h3>
        <p>
          The authentication system features a 50/50 split-screen layout. The left side showcases an automated 4-slide carousel highlighting benefits for Donors, NGOs, and Volunteers with 3+2 circular feature badges and a central vertical pill indicator. The right side provides both password-based access and 1-click evaluator demo logins.
        </p>

        <h3 class="subsection-heading">3.2 Automated Batch ID Issuance & Expiry Tracking</h3>
        <p>
          Donors list surplus food with preparation timestamps, consumption deadlines, storage requirements, and meal portions. The system computes real-time freshness countdowns, filtering out expired batches using compound B-Tree indexes (<code class="inline-code">status</code>, <code class="inline-code">availableUntil</code>).
        </p>

        <h3 class="subsection-heading">3.3 Engine-Level $jsonSchema Validation Rules</h3>
        <p>
          MongoDB enforces document structure validation at the database layer. Quantities less than or equal to zero and invalid status enumerations are rejected natively with <code class="inline-code">WriteError (Code: 121)</code>:
        </p>
        <div class="code-box">DONATIONS_SCHEMA = {{
    "$jsonSchema": {{
        "bsonType": "object",
        "required": ["donorId", "foodName", "category", "quantityKg", "status"],
        "properties": {{
            "quantityKg": {{"bsonType": ["double", "int", "decimal"], "minimum": 0.1}},
            "status": {{"enum": ["available", "requested", "assigned", "delivered", "cancelled"]}}
        }}
    }}
}}</div>
      </div>
    </div>

    <div class="running-footer">
      <span>FoodRescue Technical Project Report</span>
      <span>Page 3</span>
    </div>
  </div>


  <!-- =========================================================================
       PAGE 4: ATOMIC CLAIMS & SCREENSHOTS (EXACT MATCH TO PAGE 4)
  ========================================================================== -->
  <div class="page">
    <div>
      <div class="running-header">
        <span>FOODRESCUE | TECHNICAL PROJECT REPORT</span>
        <span>CSE 494 - INTELLIGENT NOSQL DATABASES</span>
      </div>

      <div class="page-content">
        <h3 class="subsection-heading">3.4 Concurrency-Safe Atomic Claims & Courier Dispatch</h3>
        <p>
          To prevent duplicate claiming while preserving real-time allocation, FoodRescue executes atomic <code class="inline-code">find_one_and_update</code> queries directly at the database engine:
        </p>
        <div class="code-box">updated_task = db.delivery_tasks.find_one_and_update(
    {{"_id": ObjectId(task_id), "status": "pending_assignment", "volunteerId": None}},
    {{"$set": {{"status": "accepted", "volunteerId": current_user["_id"]}}}},
    return_document=ReturnDocument.AFTER
)</div>
        <p>
          The <code class="inline-code">donations</code> collection enforces a Compound B-Tree Index on <code class="inline-code">(status, availableUntil)</code>:
        </p>
        <div class="code-box">db.donations.create_index([("status", 1), ("availableUntil", 1)])</div>
        <p>
          Attempting concurrent claiming triggers an immediate <code class="inline-code">HTTP 409 Conflict</code> without corrupting inventory records.
        </p>

        <div class="figure-container">
          <img src="{img_login}" class="figure-img" style="max-height: 155px;" alt="Auth Interface" />
          <div class="figure-caption">Figure 2. Sliding Split-Screen Authentication & Benefits Showcase</div>
        </div>

        <div class="figure-container">
          <img src="{img_browse}" class="figure-img" style="max-height: 155px;" alt="Browse Catalog" />
          <div class="figure-caption">Figure 3. Food Catalog & Available Meal Batches for NGO Claiming</div>
        </div>
      </div>
    </div>

    <div class="running-footer">
      <span>FoodRescue Technical Project Report</span>
      <span>Page 4</span>
    </div>
  </div>


  <!-- =========================================================================
       PAGE 5: SEGREGATED PORTALS & AGGREGATIONS (EXACT MATCH TO PAGE 5)
  ========================================================================== -->
  <div class="page">
    <div>
      <div class="running-header">
        <span>FOODRESCUE | TECHNICAL PROJECT REPORT</span>
        <span>CSE 494 - INTELLIGENT NOSQL DATABASES</span>
      </div>

      <div class="page-content">
        <h3 class="subsection-heading">3.5 Segregated Portals & Role-Based Workspaces</h3>
        <p>
          The portal provides isolated role workspaces: Donors create listings, NGOs submit claims, Volunteers accept delivery runs, and Administrators audit systemic transactions:
        </p>
        <ol>
          <li><strong>Donor Portal</strong>: Post surplus batches with automatic dietary tags and expiry limits.</li>
          <li><strong>Shelter Portal</strong>: Atomic reservation of fresh batches and live receipt confirmation.</li>
          <li><strong>Courier Workspace</strong>: Accept available pickup runs, view route zones, and earn points.</li>
          <li><strong>Admin Console</strong>: Live aggregation charts, NGO compliance verification, and audit logs.</li>
        </ol>

        <div class="figure-container">
          <img src="{img_donor}" class="figure-img" style="max-height: 155px;" alt="Donor Dashboard" />
          <div class="figure-caption">Figure 4. Donor Dashboard & Real-Time Food Listing Management</div>
        </div>

        <h3 class="subsection-heading">3.6 Multi-Stage MongoDB Aggregation Pipelines</h3>
        <p>FoodRescue implements six advanced aggregation pipelines in <code class="inline-code">aggregations.py</code>:</p>
        <ul>
          <li><strong>1. Rescued Food Timeline Trend</strong>: Uses <code class="inline-code">$match</code>, <code class="inline-code">$project</code> (<code class="inline-code">$dateToString</code>), and <code class="inline-code">$group</code> by date.</li>
          <li><strong>2. Top Food Donors</strong>: Employs <code class="inline-code">$group</code>, <code class="inline-code">$lookup</code> with <code class="inline-code">users</code>, and <code class="inline-code">$unwind</code> to sum donated weights.</li>
          <li><strong>3. Volunteer Leaderboard</strong>: Joins user data, sorts by <code class="inline-code">totalPoints</code> descending, and limits to top 10.</li>
          <li><strong>4. Courier Verification Metric</strong>: Aggregates confirmed delivery tasks to audit volunteer profiles.</li>
          <li><strong>5. Category & Status Breakdown</strong>: Multi-key grouping on <code class="inline-code">(category, status)</code> for pie charts.</li>
          <li><strong>6. NGO Fulfillment Rates</strong>: Calculates percentage ratios using <code class="inline-code">$divide</code> and conditional sums.</li>
        </ul>
      </div>
    </div>

    <div class="running-footer">
      <span>FoodRescue Technical Project Report</span>
      <span>Page 5</span>
    </div>
  </div>


  <!-- =========================================================================
       PAGE 6: REAL-TIME CHARTS & BENCHMARKS (EXACT MATCH TO PAGE 6)
  ========================================================================== -->
  <div class="page">
    <div>
      <div class="running-header">
        <span>FOODRESCUE | TECHNICAL PROJECT REPORT</span>
        <span>CSE 494 - INTELLIGENT NOSQL DATABASES</span>
      </div>

      <div class="page-content">
        <div class="figure-container">
          <img src="{img_admin}" class="figure-img" style="max-height: 170px;" alt="Admin Analytics" />
          <div class="figure-caption">Figure 5. Real-Time Analytics Dashboard & Live Aggregation Charts</div>
        </div>

        <h2 class="section-heading">4. Benchmark Setup and Results</h2>
        <p>
          A quantitative benchmark was conducted on a synthetic dataset of approximately 10,000 documents to evaluate surplus food listing lookup. The query was measured before and after creating the compound index on <code class="inline-code">(status, availableUntil)</code>.
        </p>

        <table class="data-table">
          <thead>
            <tr>
              <th>Metric</th>
              <th>Before index</th>
              <th>After index</th>
              <th>Observed change</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Median query latency</strong></td>
              <td>62.40 ms</td>
              <td>1.65 ms</td>
              <td><strong>97.35% lower</strong></td>
            </tr>
            <tr>
              <td><strong>Documents examined</strong></td>
              <td>10,000</td>
              <td>1</td>
              <td><strong>99.99% fewer</strong></td>
            </tr>
            <tr>
              <td><strong>Execution behaviour</strong></td>
              <td>COLLSCAN</td>
              <td>IXSCAN</td>
              <td>Index used for this query</td>
            </tr>
          </tbody>
        </table>

        <h3 class="subsection-heading">4.1 Interpretation</h3>
        <p>
          Adding the compound index reduced median measured latency from 62.40 ms to 1.65 ms and reduced documents examined from 10,000 to 1. This indicates that MongoDB examined far fewer documents by performing a B-Tree index scan (<code class="inline-code">IXSCAN</code>) instead of a full collection scan (<code class="inline-code">COLLSCAN</code>). Results may vary with hardware, cache state, database load, data distribution, and query shape.
        </p>
      </div>
    </div>

    <div class="running-footer">
      <span>FoodRescue Technical Project Report</span>
      <span>Page 6</span>
    </div>
  </div>


  <!-- =========================================================================
       PAGE 7: CERTIFICATE, SECURITY & CONCLUSION (EXACT MATCH TO PAGE 7)
  ========================================================================== -->
  <div class="page">
    <div>
      <div class="running-header">
        <span>FOODRESCUE | TECHNICAL PROJECT REPORT</span>
        <span>CSE 494 - INTELLIGENT NOSQL DATABASES</span>
      </div>

      <div class="page-content">
        <div class="figure-container">
          <img src="{img_cert}" class="figure-img" style="max-height: 155px;" alt="Volunteer Certificate" />
          <div class="figure-caption">Figure 6. Official Printable Humanitarian Volunteer Certificate</div>
        </div>

        <h2 class="section-heading">5. Security and Limitations</h2>
        <p>
          The application includes JWT verification, password salt hashing, protected API endpoints, user-specific portals, and atomic checks for claim operations. Credentials are kept in local environment files (<code class="inline-code">.env</code>) and never committed to the public repository.
        </p>
        <p>
          FoodRescue is an academic prototype. Real-world commercial scaling would require MongoDB Replica Sets with sharding, dedicated SMS gateways for couriers, and rate-limiting middleware to guard against denial-of-service surges.
        </p>

        <h2 class="section-heading">6. Conclusion and Future Scope</h2>
        <p>
          FoodRescue combines MongoDB query execution, engine-level schema validation, compound index integrity, and multi-stage aggregation pipelines in one web application. The project demonstrates full-stack development concepts including Flask REST APIs, PyMongo integration, JWT authentication, and reactive React visualizations.
        </p>
        <p>
          The recorded benchmark showed an improvement for the tested query after adding an index on <code class="inline-code">(status, availableUntil)</code>. Future work may include AI route bundling, IoT cold-chain temperature sensors, and public blockchain ledger anchoring.
        </p>

        <h3 class="subsection-heading">References</h3>
        <ul>
          <li><strong>MongoDB Manual &mdash; Indexes</strong>: <span style="color:#0369a1;">https://www.mongodb.com/docs/manual/indexes/</span></li>
          <li><strong>MongoDB Manual &mdash; Aggregation Pipeline</strong>: <span style="color:#0369a1;">https://www.mongodb.com/docs/manual/core/aggregation-pipeline/</span></li>
          <li><strong>PyMongo Documentation</strong>: <span style="color:#0369a1;">https://pymongo.readthedocs.io/</span></li>
          <li><strong>Flask Documentation</strong>: <span style="color:#0369a1;">https://flask.palletsprojects.com/</span></li>
        </ul>

        <h3 class="subsection-heading">GitHub Repository</h3>
        <p>
          Project repository: <strong style="color: #1e3a8a;">https://github.com/Manikanta-2006/foodRescue</strong>
        </p>
      </div>
    </div>

    <div class="running-footer">
      <span>FoodRescue Technical Project Report</span>
      <span>Page 7</span>
    </div>
  </div>

</body>
</html>
"""

    output_html = os.path.join(base_dir, "FoodRescue_Project_Report_Printable.html")
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Generated HTML report: {output_html}")

    # Now generate PDF using headless Chrome
    output_pdf = os.path.join(base_dir, "FoodRescue_Technical_Project_Report.pdf")
    chrome_cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf}",
        f"file://{output_html}"
    ]

    print("Running Chrome to generate PDF...")
    result = subprocess.run(chrome_cmd, capture_output=True, text=True)
    if result.returncode == 0 and os.path.exists(output_pdf):
        print(f"Successfully generated PDF: {output_pdf} (Size: {os.path.getsize(output_pdf)} bytes)")
    else:
        print(f"Chrome PDF generation error: {result.stderr}")

if __name__ == "__main__":
    generate_report()

