<link rel="stylesheet" href="../style.css">

<script>
  // A tiny delay ensures VS Code has finished rendering the HTML elements
  setTimeout(() => {
      const expandableItems = document.querySelectorAll('.toc-sidebar > ul > li > ul > li:has(> ul)');

      expandableItems.forEach(item => {
          item.addEventListener('click', function(event) {
              // Ensure the click happened directly on the list item or arrow
              if (event.target.tagName !== 'A' || event.target.parentElement === this) {
                  this.classList.toggle('is-open');
              }
          });
      });
  }, 300); // Waits 300 milliseconds before attaching the clicks
</script>

<div class="toc-sidebar">

<strong>Other Files</strong>

- <a href="complex_sentences.md">Complex Sentences</a>
- <a href="future_actions.md">Future Actions</a>
- <a href="modals.md">Modals</a>
- <a href="passive.md">Passive Sentences</a> 
- <a href="tenses.md">Tenses</a>

<strong>Table of Contents</strong>

- [News \& Reporting](#news--reporting)
  - [News](#news)
    - [Reporting](#reporting)
    - [Near future announcements](#near-future-announcements)
- [Storytelling \& Narratives](#storytelling--narratives)
  - [Storytelling](#storytelling)
  - [Narratives](#narratives)
    - [Retelling](#retelling)
    - [Sudden event](#sudden-event)
  - [Retelling hearing/speech](#retelling-hearingspeech)
- [Media](#media)
  - [Content discussion](#content-discussion)
  - [Live commentaries](#live-commentaries)

</div>

<div class="main-content">

# News & Reporting
## News
### Reporting
- **Present perfect & past simple**  

  Use the **present perfect** to give **background knowledge** or introduce the lead, then switch to the **past simple** to provide specific **subsequent details.**

  > *A Russian spacecraft **has returned** safely to Earth with its two passengers. US astronaut Scott Keane and Russian cosmonaut Olga Kaleri **landed** in the early hours of Wednesday.*

### Near future announcements
- **Be to + infinitive**  
  To talk about planned events that **can be controlled by people** in the **near future**. 

  > *Police officers **are to visit** every home in the area.*

# Storytelling & Narratives
## Storytelling
- **Present tense**  
  Use the **present simple** to create the impression that events in an informal story or joke are happening right now. 
 
  > *She **goes** up to this man and **looks** straight into his eyes. He's not **wearing** his glasses, and he **doesn't recognise** her...*

## Narratives   
### Retelling
- **Past tense**  
  It is generally used in **fictions**.  

  **Past perfect** is used to establish **short, consecutive actions,** before a past point, and **past perfect continuous** is to establish **ongoing**, long term actions. 
  
  > *The body of a climber who went missing in the Alps was finally found yesterday. Carl Sims **had been climbing** along near the Harz Waterfall, which has claimed many lives in the past.*

### Sudden event
- **Past tense & present simple**  
  Often used **after a past tense setup** alongside certain phrases to create **immediate drama**.

  - *Suddenly* 
  - *All of a sudden* 

  > *I was sitting in the park, reading a newspaper, when **all of a sudden** this dog **jumps** at me.*

## Retelling hearing/speech
- **Present simple**  
  To introduce news that we **have heard, read, seen, or being told**.

  - *It says here*
  - *I hear/gather/see/understand* 
  - *They say, (Someone) says, (Someone) tells me*.

  > *I **gather** you're worried about Pedro.*

- **Past simple/perfect**  
  Often used in **reporting** what was originally **said or thought** in the present perfect or past simple.

  > *I was sure that I **had met** him before.*

  > *Police said that 225 people **had drowned/drowned** in the recent flood.*

- **Passive sentences** are often used in formal reports, see: <a href="./passive.md">Passive sentence</a>
  

# Media
## Content discussion
- **Present simple**  
  To refer to the **contents** of books, films, newspapers, etc.

  > *Thompson **gives** a list of the largest European companies in Chapter 6.*

## Live commentaries
- **Present continuous**  
  Used when the report takes place at the **same time as the action** (for example, on sport events).





</div>