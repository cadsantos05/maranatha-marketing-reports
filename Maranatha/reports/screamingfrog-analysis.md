# Screaming Frog Analysis — Maranatha Stone and Floors
**Source files:** page_titles_all.csv, meta_description_all.csv, h1_all.csv, h2_all.csv
**Total pages crawled:** 59 (58 indexable + 1 non-indexable)
**Analysis Date:** March 2026

---

## Summary of Issues Found

| Issue Type | Count |
|---|---|
| Missing meta descriptions | 34 pages |
| Duplicate page titles | 6 blog pagination pages |
| Page titles too long (>600px) | 13 pages |
| Page titles truncated/broken | 2 pages |
| WordPress default "Archive" titles | 4 pages |
| H1s with zero keyword value (≤15 chars) | 15 pages |
| Duplicate H1 ("Blog.") | 6 pages |
| Duplicate H2 ("Request an Appointment.") | 38 pages |
| Pages missing Birmingham keyword in H1 | 13 service/core pages |
| Critical title tag bugs | 2 pages |

---

## 1. Duplicate Page Titles

### Blog Pagination (6 pages — same title)
All blog archive pages share the identical title tag:
**"Countertop & Flooring Insights | Birmingham, AL | Maranatha"**

| Page |
|---|
| maranatha.pro/blog/ |
| maranatha.pro/blog/page/2/ |
| maranatha.pro/blog/page/3/ |
| maranatha.pro/blog/page/4/ |
| maranatha.pro/blog/page/5/ |
| maranatha.pro/blog/page/6/ |

**Fix:** Blog pagination pages 2–6 should either be set to `noindex` (recommended — pagination pages have no standalone SEO value) or given canonical tags pointing to the main blog page. The main blog page title is fine.

---

## 2. Missing Meta Descriptions (34 Pages)

### Service / Core Pages (High Priority)
| Page | URL |
|---|---|
| Products Hub | /products/ |
| Projects | /projects/ |
| Commercial Projects | /project-category/commercial/ |
| Residential Projects | /project-category/residential/ |

### Project Detail Pages (Medium Priority)
| Page | URL |
|---|---|
| Dagny | /projects/dagny/ |
| Sinks Residence | /projects/sample-residential-project-3/ |
| Ajlouny Residence | /projects/sample-residential-project-1/ |
| Fennec | /projects/sample-commercial-project-4/ |
| Sims Residence | /projects/sample-residential-project-2/ |
| Mercantile on Morris | /projects/mercantile-on-morris/ |
| New Ideal | /projects/new-ideal/ |

### Blog Posts Missing Meta (High Priority — 23 posts)
| Post Title | URL |
|---|---|
| The Benefits of Choosing Local Stone Fabricators | /the-benefits-of-choosing-local-stone-fabricators-for-your-next-remodel/ |
| 2025 Stone Countertop Trends Forecast | /2025-stone-countertop-trends-forecast-whats-next-in-home-design/ |
| How to Take Care of Your Countertops During the Holidays | /how-to-take-care-of-your-countertops-during-the-holidays-tips-for-a-stress-free-season/ |
| Innovative Tile Designs to Transform Your Home | /innovative-tile-designs-to-transform-your-home/ |
| Elevate Your Kitchen in 2024 | /elevate-your-kitchen-in-2024-top-trends-and-tips-for-countertops-tiles-and-flooring/ |
| Can You Put Hot Pans on Granite? | /can-you-put-hot-pans-on-granite-the-dos-and-donts/ |
| 5 Trending Flooring Styles | /5-trending-flooring-styles-to-elevate-your-homes-aesthetic/ |
| The Ultimate Guide to Choosing the Perfect Countertop | /the-ultimate-guide-to-choosing-the-perfect-countertop-for-your-kitchen/ |
| The Importance of Professionalism Installation | /the-importance-of-professionalism-installation-for-stone-and-flooring-projects/ |
| The Importance of Professional Stone Installation | /the-importance-of-professional-stone-installation-what-to-expect/ |
| Recap of 2024 Stone Design Trends | /recap-of-2024-stone-design-trends-what-we-loved-and-whats-here-to-stay/ |
| Differences Between Granite, Quartz, and Marble | /differences-between-granite-quartz-and-marble-countertops/ |
| Kitchen Design Trends, 2023 | /kitchen-design-trends-2023-what-you-need-to-know/ |
| Quartzite Care & Maintenance | /quartzite-care-maintenance/ |
| What's Special about June & July ('23)? | /whats-special-about-june-july-23/ |
| Kitchen & Bathroom Design Trends: Enhancing Your Home in Alabama | /kitchen-bathroom-design-trends-enhancing-your-home-in-alabama/ |
| Dekton and Your Bathroom | /dekton-and-your-bathroom/ |
| Do's and Don'ts: A Quick Guide for Alabama Homeowners | /dos-and-donts-a-quick-guide-for-alabama-homeowners/ |
| Most Requested Countertops for Kitchen Renos | /most-requested-countertops-for-kitchen-renos/ |
| Timeless Beauty of Granite | /timeless-beauty-of-granite/ |
| Dekton Countertops | /dekton-new-kid-on-the-block/ |
| Quartz Care & Maintenance | /maranatha-quartz-care-maintenance/ |
| What Are Sculleries & Why Care? | /what-are-sculleries-why-care/ |

**Note:** 23 out of 27 blog posts are missing meta descriptions. This is a site-wide pattern, not isolated incidents.

---

## 3. Title Tag Issues

### Critical Bugs
| Issue | Page | Current Title |
|---|---|---|
| Duplicated word | /products/sapienstone/ | "**PorcelainPorcelain** Countertops in Birmingham, AL \| Maranatha" |
| One-word title | /products/neolith/ | "**Dialtile**" (8 chars, 62px) |

### WordPress Default "Archive" Titles (No keyword value)
| Page | Current Title |
|---|---|
| /products/ | "Products Archive - Maranatha Granite" |
| /projects/ | "Projects Archive - Maranatha Granite" |
| /project-category/commercial/ | "Commercial Archives - Maranatha Granite" |
| /project-category/residential/ | "Residential Archives - Maranatha Granite" |

### Titles Too Long (>600px — will be truncated in Google)
| Page | Title | Pixel Width |
|---|---|---|
| /how-to-take-care-of-your-countertops-during-the-holidays-... | "How to Take Care of Your Countertops During the Holidays: Tips for a Stress-Free Season - Maranatha Granite" | 978px |
| /elevate-your-kitchen-in-2024-... | "Elevate Your Kitchen in 2024: Top Trends and Tips for Countertops, Tiles, and Flooring - Maranatha Granite" | 947px |
| /the-importance-of-professionalism-installation-... | "The Importance of Professionalism Installation for Stone and Flooring Projects - Maranatha Granite" | 883px |
| /recap-of-2024-stone-design-trends-... | "Recap of 2024 Stone Design Trends: What We Loved and What's Here to Stay - Maranatha Granite" | 870px |
| /products/granite-marble-quartzite/ | "Natural Stone Countertops in Birmingham, AL \| Maranatha" | 518px ✓ |
| /the-importance-of-professional-stone-installation-... | "The Importance of Professional Stone Installation: What to Expect - Maranatha Granite" | 771px |
| /differences-between-granite-quartz-and-marble-countertops/ | "Differences Between Granite, Quartz, and Marble Countertops - Maranatha Granite" | 734px |
| /5-trending-flooring-styles-... | "5 Trending Flooring Styles to Elevate Your Home's Aesthetic - Maranatha Granite" | 717px |
| /large-format-tiles-... | "Benefits of Installing Large-Format Tiles in Modern Homes - Maranatha Granite" | 705px |
| /can-you-put-hot-pans-on-granite-... | "Can You Put Hot Pans on Granite? The Do's and Don'ts - Maranatha Granite" | 667px |
| /the-ultimate-guide-to-choosing-... | "The Ultimate Guide to Choosing the Perfect Countertop for Your Kitchen -" | 654px |
| /kitchen-design-trends-2023-... | "Kitchen Design Trends, 2023: What You Need to Know - Maranatha Granite" | 664px |
| /the-benefits-of-choosing-local-stone-fabricators-... | "The Benefits of Choosing Local Stone Fabricators for Your Next Remodel - Maranatha Granite" | 831px |

**Root cause:** Blog post titles append "- Maranatha Granite" which adds ~150px and pushes most posts over the limit. Either shorten the post titles or remove the brand suffix from blog title tags.

### Truncated / Broken Titles
| Page | Issue |
|---|---|
| /the-ultimate-guide-to-choosing-the-perfect-countertop-for-your-kitchen/ | Title ends with a bare dash: "...for Your Kitchen **-**" — content after dash is missing |
| /can-quartz-countertops-burn/ | Title appears cut off: "...What Birmingham Homeowners **S**" — truncated mid-word |

---

## 4. H1 Analysis

### No Missing H1s
All 58 indexable pages have exactly one H1 tag. No missing H1s.

### Duplicate H1: "Blog." (6 pages)
| Page |
|---|
| /blog/ |
| /blog/page/2/ |
| /blog/page/3/ |
| /blog/page/4/ |
| /blog/page/5/ |
| /blog/page/6/ |

**Fix:** Same as title — noindex pagination pages 2–6.

### H1s With Zero Keyword Value (single word or generic label)
These H1s provide no SEO signal. Google weighs H1 heavily for topical relevance.

| Page | Current H1 | Length |
|---|---|---|
| /blog/ | "Blog." | 5 |
| /about-us/ | "About." | 6 |
| /products/dekton/ | "Dekton." | 7 |
| /products/ | "Products." | 9 |
| /projects/ | "Projects." | 9 |
| /contact/ | "Contact." | 8 |
| /showroom/ | "Showroom." | 9 |
| /products/cambria/ | "Cambria." | 8 |
| /products/hanstone/ | "HanStone." | 9 |
| /products/neolith/ | "Dialtile." | 9 |
| /products/sapienstone/ | "Porcelain." | 10 |
| /project-category/commercial/ | "Commercial." | 11 |
| /project-category/residential/ | "Residential." | 12 |
| /products/granite-marble-quartzite/ | "Natural Stones." | 15 |
| /recent-projects/ | "Recent Project." | 15 |

**Pattern:** Every core service page and product page has a 1–2 word H1 with no keyword or location targeting. This is a site-wide template issue.

### H1s That Are Well Optimized (keep these as reference)
| Page | H1 |
|---|---|
| Homepage | "Custom Countertops & Flooring in Birmingham, AL." ✓ |
| /products/silestone/ | "Silestone Quartz Countertops in Birmingham, AL." ✓ |
| /how-much-countertop-installation-cost-birmingham-al/ | "How Much Does Countertop Installation Cost in Birmingham, AL?" ✓ |

---

## 5. Pages Needing Birmingham Keyword Optimization

Cross-referenced against keywords.md primary targets. These service pages have no Birmingham, AL signal in their H1:

| Page | Current H1 | Recommended H1 |
|---|---|---|
| /products/ | "Products." | "Stone Countertops & Flooring — Birmingham, AL" |
| /products/granite-marble-quartzite/ | "Natural Stones." | "Natural Stone Countertops in Birmingham, AL" |
| /products/flooring/ | "Hardwood & Tile Flooring." | "Hardwood, Tile & Vinyl Flooring in Birmingham, AL" |
| /products/hanstone/ | "HanStone." | "HanStone Quartz Countertops in Birmingham, AL" |
| /products/cambria/ | "Cambria." | "Cambria Quartz Countertops in Birmingham, AL" |
| /products/dekton/ | "Dekton." | "Dekton Countertops in Birmingham, AL" |
| /products/sapienstone/ | "Porcelain." | "Porcelain Countertops in Birmingham, AL" |
| /products/neolith/ | "Dialtile." | "Tile Surfaces in Birmingham, AL" |
| /showroom/ | "Showroom." | "Countertop Showroom in Birmingham, AL" |
| /projects/ | "Projects." | "Countertop & Flooring Projects — Birmingham, AL" |
| /recent-projects/ | "Recent Project." | "Recent Countertop & Flooring Installations — Birmingham, AL" |
| /about-us/ | "About." | "About Maranatha Stone and Floors — Birmingham, AL" |
| /contact/ | "Contact." | "Contact Maranatha Stone and Floors — Birmingham, AL" |

---

## 6. H2 Pattern Issue — "Request an Appointment."

"Request an Appointment." appears as an H2 on **38 out of 58 pages** — it is a sitewide template element being rendered as a heading tag. While not a ranking penalty, this dilutes the semantic signal of H2s across the site. It should be converted to a styled `<p>` or `<div>` element, not an `<h2>`.

---

## 7. Meta Description Over Character Limit

| Page | Length | Issue |
|---|---|---|
| /large-format-tiles-.../ | 469 chars | Extremely over limit — reads like dumped keywords followed by intro paragraph. This appears to be a copy-paste error where keywords and article intro were concatenated into the meta field. |

Recommended max: 155–160 characters.

---

## 8. Priority Fix List

### Fix Immediately (Week 1)
| # | Action | Page(s) |
|---|---|---|
| 1 | Fix "PorcelainPorcelain" title bug | /products/sapienstone/ |
| 2 | Fix "Dialtile" one-word title and meta mismatch | /products/neolith/ |
| 3 | Fix truncated title ending in "-" | /the-ultimate-guide-to-choosing-.../ |
| 4 | Fix truncated title ending mid-word | /can-quartz-countertops-burn/ |
| 5 | Fix 469-char meta description | /large-format-tiles-.../ |
| 6 | Rewrite 4 WordPress "Archive" title tags | /products/, /projects/, /project-category/commercial/, /project-category/residential/ |

### Fix This Month (Weeks 2–4)
| # | Action | Scope |
|---|---|---|
| 7 | Rewrite H1s on all 15 single-word/generic pages | Add keyword + location |
| 8 | Add meta descriptions to 4 service/category pages | /products/, /projects/, etc. |
| 9 | Add meta descriptions to top-priority blog posts | "Can You Put Hot Pans on Granite", "Differences Between Granite/Quartz/Marble", "Quartzite Care", "Hot Countertop Guide" |
| 10 | Noindex blog pagination pages 2–6 | Removes 5 duplicate titles and 5 duplicate H1s in one fix |
| 11 | Remove "- Maranatha Granite" from blog post titles OR shorten post titles to stay under 600px | 13 posts currently over limit |

### Fix Next Month
| # | Action | Scope |
|---|---|---|
| 12 | Add meta descriptions to remaining 19 blog posts | Full blog coverage |
| 13 | Convert "Request an Appointment." from H2 to non-heading element | Sitewide template fix |
| 14 | Update "Maranatha Granite" brand references to "Maranatha Stone and Floors" | All title tags and schema |
