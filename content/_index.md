---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        BioMed Communications
      image:
        filename: biomedcom.jpg
      text: |
        <br>
        
        這裡分享有關免疫治療、放射治療、標靶核種治療、腎臟病學、數據科學和系統生物學應用的資訊和知識。 
  
  - block: collection
    content:
      title: Latest Posts
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: compact
      columns: '1'
  
 # - block: markdown
 #   content:
  #    title:
   #   subtitle: ''
    #  text:
   # design:
    #  columns: '1'
     # background:
      #  image: 
       #   filename: chemical.jpg
        #  filters:
         #   brightness: 1
          #parallax: false
          #position: center
         # size: cover
         # text_color_light: true
      #spacing:
       # padding: ['20px', '0', '20px', '0']
     # css_class: fullscreen

 # - block: collection
  #  content:
    #  title: Latest Preprints
   #   text: ""
   #   count: 5
   #   filters:
    #    folders:
    #      - publication
     #   publication_type: 'article'
    #design:
    #  view: citation
    #  columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="團隊人物 →" %}}
    design:
      columns: '1'
  - block: tag_cloud
    content:
      title: 主題標籤
      subtitle: 
      text: 
      # Choose a taxonomy from the `taxonomies` list in `config.yaml` to display (e.g. tags, categories, authors)
      taxonomy: tags
      # Choose how many tags you would like to display (0 = all tags)
      count: 20
    design:
      # Minimum and maximum font sizes (1.0 = 100%).
      font_size_min: 0.7
      font_size_max: 2.0
---
