---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2022-10-24
type: landing

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      text: ''
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/cv_Farren.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: 'My Research'
      subtitle: ''
      text: |-
        I work on cosmology — extracting insights about fundamental physics from the largest datasets we have about the Universe. My focus is **cross-correlating** observations from different surveys, leveraging complementary information to mitigate biases that any single survey would carry alone. In practice, that means combining gravitational lensing of the Cosmic Microwave Background with galaxy surveys to map structure across cosmic time.

        Day-to-day, my work sits at the intersection of statistics, scientific computing, and large data: Bayesian inference at scale, distributed and high-performance computing, and end-to-end analysis pipelines that thread careful systematics control from raw observations to published constraints. The same toolkit transfers naturally beyond cosmology — to any setting that demands rigorous inference, robust software engineering, and the ability to extract subtle signals from massive, noisy data.

        I lead and contribute to analyses across the [Simons Observatory (SO)](https://simonsobservatory.org/), [Dark Energy Spectroscopic Instrument (DESI)](https://www.desi.lbl.gov/), and the Atacama Cosmology Telescope (ACT) collaborations, and I am also a member of [LSST DESC](https://www.lsstdesc.org/).
    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2
  - block: collection
    content:
      title: Recent Publications
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation
  - block: collection
    id: news
    content:
      title: Recent News
      subtitle: ''
      text: 'See [all news →](/blog/)'
      # Page type to display. E.g. post, talk, publication...
      page_type: blog
      # Choose how many pages you would like to display (0 = all pages)
      count: 3
      # Filter on criteria
      filters:
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: card
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
---
