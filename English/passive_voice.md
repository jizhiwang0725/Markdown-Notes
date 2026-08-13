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








- <a href="communication.md">Communication</a>
- <a href="complements.md">Complements</a>
- <a href="complex_structures.md">Complex Structures</a>
- <a href="future_actions.md">Future Actions</a>
- <a href="prepositions.md">Prepositions</a>
- <a href="tenses.md">Tenses</a>
- <a href="verbs.md">Verbs</a>

<strong>Table of Contents</strong>

- [Active and Passive Voice](#active-and-passive-voice)
  - [Purpose](#purpose)
  - [Pattern overview](#pattern-overview)
    - [Basic verb structure](#basic-verb-structure)
    - [Advanced verb structure](#advanced-verb-structure)
  - [Tenses and modals](#tenses-and-modals)
    - [Standard tenses](#standard-tenses)
    - [With modals](#with-modals)
  - [Object complements](#object-complements)
  - [Advanced verb structure](#advanced-verb-structure-1)
    - [Ditransitive](#ditransitive)
    - [Complex verb chains](#complex-verb-chains)
- [Limitations of Passive Voice](#limitations-of-passive-voice)
  - [Intransitive verbs](#intransitive-verbs)
  - [Linking verbs](#linking-verbs)
  - [Certain stative verbs](#certain-stative-verbs)
    - [Mental and abstract](#mental-and-abstract)
    - [Possessive and objective](#possessive-and-objective)
    - [Desires](#desires)
  - [Reflexive and reciprocal objects](#reflexive-and-reciprocal-objects)
  - [Idioms and body parts](#idioms-and-body-parts)
- [Practical Usage of Passive Voice](#practical-usage-of-passive-voice)
  - [General contexts](#general-contexts)
    - [Agent and instrument](#agent-and-instrument)
    - [Omitting agent or instrument](#omitting-agent-or-instrument)
  - [Formal contexts and writing](#formal-contexts-and-writing)
    - [Factual writing](#factual-writing)
    - [Writing structure](#writing-structure)
    - [Formal speeches](#formal-speeches)
  - [Reporting](#reporting)
    - [Receiver required](#receiver-required)
    - [Receiver not required](#receiver-not-required)

</div>

<div class="main-content">

# Active and Passive Voice
## Purpose
- Invented to answer the question: **"What happened to this object?"**
- To remove or ignore the **doer**, and to focus on the **object** by saying the direct object first.  

## Pattern overview
### Basic verb structure
| Category | Active | Passive |
| --- | --- | --- |
| **Transitive** | V + DO | DO + be + PP |

### Advanced verb structure
| Category | Active | Passive |
| --- | --- | --- |
| **Ditransitive**<br> *(Germanic)* | V + IO + DO | IO + be + PP + DO |
|| V + DO + prep + IO | DO + be + PP + prep + IO |
| *(Latin)* | V + DO + prep + IO | DO + be + PP + prep |
| **Object Complement** | V + O + complement | O + be + PP + complement |
| **Complex Verb Chain**<br> *(Bare Infinitive)* | V + O + bare infinitive | O + be + to infinitive | 
| *(Continuous Verbs)* | V + O + -ing | O + be + PP + -ing |
| *(Gerund Phrase)* | V + gerund phrase | V + being + PP | 
| *(to infinitive)* | V + O + to infinitive | O + be + PP + to infinitive |
|| V + to infinitive + O | O + V + to be + PP<br> **(:warning: The meaning could be changed)** | 

## Tenses and modals
### Standard tenses
| Tense | Example | Passive | Example |
| --- | --- | --- | --- |
| **Present simple** | *John **tells** me that you're thinking of leaving.* | am/is/are | *I **am told** (by John) that you're thinking of leaving.* |
| **Past simple** | *John **told** me that you were leaving.* | was/were | *I **was told** (by John) that you were leaving.* |
| **Present perfect** | *John **has told** me that you are leaving.* | have/has been | *I **have been told** (by John) that you are leaving.* |
| **Past perfect** | *John **had** already **told** me that you were leaving.* | had been | *I **had** already **been told** (by John) that you were leaving.* |
| **Present continuous** | *John **is** always **telling** me that you are leaving.* | am/is/are being | *I **am** always **being told** (by John) that you are leaving.* |
| **Past continuous** | *John **was** always **telling** me that you were leaving.* | was/were being | *I **was** always **being told** (by John) that you were leaving.* |
| **Future simple** | *I **will tell** John that you are leaving.* | will be | *John **will be told** (by me) that you are leaving.* |
| **Future perfect** | *By tomorrow I **will have told** John that you are leaving.* | will have been | *By tomorrow John **will have been told** (by me) that you are leaving.* |
| **Present perfect continuous**<br> *(rare in the passive)* | *John **has been telling** me for ages that you are leaving.* | has/have been being | *I **have been being told** (by John) for ages that you are leaving.* |

### With modals 
| Tense | Example | Passive | Example (Past Participle) |
| --- | --- | --- | --- |
| **Present** | *You **should tell** John.* | should/could/might/ought to (etc.) **be** | *John **should be told**.* |
| **Present perfect** | *You **should have told** John.* | should/could/ might / ought to (etc.) **have been** | *John **should have been told**.* |
| **Present perfect continuous** | *You **should have been telling** John while I was outside.* | should/could/might/ought to (etc.) **have been being** | *John **should have been being told** while I was outside.* |

## Object complements
| Active | Passive |
| --- | --- |
| *They elected **(V)** her **(O)** president **(complement)**.* | *She **(O)** was **(be)** elected **(PP)** president **(complement)**.* |

## Advanced verb structure
### Ditransitive 

| Word Type | New Subject | Active | Passive |
| --- | --- | --- | --- | 
| **Germanic** | **IO** | *Alice gave **(V)** us **(IO)** the vase **(DO)**.* | *We **(IO)** were **(be)** given **(PP)** that vase **(DO)**.* | 
|| **DO** | *Alice gave **(V)** that vase **(DO)** to **(prep)** us **(IO)*** | *That vase **(DO**) was **(be)** given **(PP)** to **(prep)** us **(IO)**.* |
| **Latin** | **DO** | *He explained **(V)** the problem **(DO)** to **(prep)** me **(IO)**.* | *The problem **(DO)** was **(be)** explained **(PP)** to **(prep)** me **(IO)**.* |

### Complex verb chains 
| Category | Active | Passive |
| --- | --- | --- |
| **Bare Infinitive** | *I saw **(V)** him **(O)** steal **(bare infinitive)** the car.* | *He **(O)** was **(be)** seen **(PP)** to steal **(to infinitive)** the car.* |
| **Continuous Verb** | *They saw **(V)** the monkey **(O)** climbing **(-ing)**.* | *The monkey **(O)** was **(be)** seen **(PP)** climbing **(-ing)**.* |
| **Gerund phrase** | *I resented **(V)** Tom/Tom's winning the prize **(gerund phrase)**.* | *I resented **(V)** the prize being **(be)** won **(PP)** by Tom* |
|  **to infinitive** | *Mr Wang has taught **(V)** Peter **(O)** to sing **(to infinitive)**.* | *Peter **(O)** has been **(be)** taught **(PP)** to sing **(to infinitive)**.* |
|| *Supermarkets started **(V)** to sell **(to infinitive)** fresh pasta **(O)**.* | *Fresh pasta **(O)** started **(V)** to be **(to be)** sold **(PP)**.* |

# Limitations of Passive Voice
## Intransitive verbs
- If a verb does **NOT have a direct object** receiving the action, there is **nothing to move to the front** of the sentence, making a passive structure impossible

  > *Birds can **fly**.*

## Linking verbs
- They do NOT describe an **action happening to something**; instead, they connect the subject to a description (a complement)

  > *The soup **tastes** salty*

## Certain stative verbs 
### Mental and abstract 
- Describes a **state of being**, a **mental process**, or an **abstract experience.**  

  - *Take after, Come up against, Get something down*
  - *Resemble, Encounter, Write*

### Possessive and objective
- These are verbs **followed by a noun phrase** object and **an -ing clause** in the active voice. They **CANNOT** be transformed into passive sentences 

  - *Anticipate, Appreciate, Dread*
  - *Forget, Recall, Remember, Mind*
  
  > *I **dread** him/his finding out*

### Desires
- Stative verbs of liking and wanting followed by an infinitive do not have a passive form.  
  - *Bear, Hate, Love*
  - *Need, Prefer, Want, Wish*

  > *Susan **liked** Karl to be there*

## Reflexive and reciprocal objects 
- If the object of the active sentence is a **reflexive pronoun** (myself, yourself, themselves) or a **reciprocal pronoun** (each other, one another).  
  
  > *She cut **herself***

## Idioms and body parts
- For actions that a subject **does with their own body parts** or for **involuntary sounds**  
  It is too **informal** and heavily focuses on the **specific person's personal** effort or physical body  
  - *Brush up on*
  - *Cast your mind back*
  - *Get something down*
  - *Take after*

  > *I **put out** a hand to steady myself* 

  > *We **came up against** a problem*

# Practical Usage of Passive Voice
## General contexts
### Agent and instrument  
- **By**  
  It is used for **agent** 

  > *The window was broken **by** the burglar.*

- **With**  
  It is used for **instrument** (the tool or material used)

  > *The window was broken **with** a hammer*

### Omitting agent or instrument
- When the **agent or instrument** is:

  - **not known**
    > *My office **was broken into** when I was on holiday*
  
  - **people in general**
    > *An order form **can be found** on page 2.*

  - **unimportant** 
    > *He **is thought to** be somewhere in Russia.*

  - **obvious**
    > *She **is being treated** in hospital*

## Formal contexts and writing
### Factual writing
- The **agent** is often **omitted**.  
  
  > *Nuclear waste will still be radioactive even after 20,000 years, so it **must be disposed of** very carefully.*

  Some verbs have **related nouns** which express the same meaning. These nouns can be used as the subject of the passive sentence 

  > *The **installation** of the new computer system will be completed by next month.*

### Writing structure
- In English, the **topic** is preferably placed at the **beginning** of a sentence and a **comment** on that topic at the **end**.  

  > *The three machines tested for the report contained different types of **safety valve**. **All the valves** were manufactured by the Boron Group in Germany.*

- It also allows **long subjects** at the **end** of a sentence.  

  > *I was surprised by **Dev's decision to give up his job and move to Sydney*** 

### Formal speeches 
- To avoid any **mention of an agent**  
  
  > *The new computer system **is being installed** next month.*

## Reporting
### Receiver required  
- **Standard passive**  
  Those verbs require an **indirect object**. The action has to be received by someone.  
  - *Encourage, Persuade, Reassure, Remind, Tell, Warn, Ask, Told*
  
  > *We **(O)** were **(be)** informed **(PP)** that we have to leave*

### Receiver not required
- **Object + be + PP + to infinitive**  
  It makes the **subject** the **topic** of the sentence.  

  :warning: Those words **DO NOT** have a **to infinitive active voice**: 
  - *Announce, Decide, Mention, Propose, Recommend, Suggest* 

  > *The damage **(O)** is **(be)** reported **(PP)** to be extensive **(to infinitive/complement)**.* 

- **It-clause**
  | Structure | Usage | Verbs | Example(s) |
  | --- | --- | --- | --- |
  | **It + be + PP + that/there-clause**<br> **There + be + PP + to be/to have been** | - Puts **important information**<br> at the **end** of the sentence. | Allege, Believe, Calculate,<br> Demonstrate, Reveal,<br> Suppose, Agree, Decide, Hope,<br> Intend, Plan, Announce,<br> Mention, Propose,<br> Recommend, Suggest | *- **It is reported that** the damage is extensive.*<br> *- **It is thought (that) there are/There are thought to be**<br> too many obstacles to peace.* |
  | **It + passive verb + wh-clause** | - To report information that<br> has been **given or found out**. | Discover, Explain, Find,<br> Know, Reveal, Show,<br> Understand | *- The decision to build the bridge was taken<br> before **it was established whether** it was<br> actually needed.* |


</div>