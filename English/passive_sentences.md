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
- <a href="complex_sentences.md">Complex Sentences</a>
- <a href="future_actions.md">Future Actions</a>
- <a href="modals.md">Modals</a>
- <a href="tenses.md">Tenses</a>

<strong>Table of Contents</strong>

- [Linking Verbs](#linking-verbs)
  - [State of being](#state-of-being)
  - [Process of change](#process-of-change)
    - [Sudden/State](#suddenstate)
    - [Gradual](#gradual)
  - [Personal guess](#personal-guess)
    - [Common verbs](#common-verbs)
    - [Description](#description)
    - [Opinions](#opinions)
- [Passive Verbs](#passive-verbs)
  - [Active to passive](#active-to-passive)
    - [With modals](#with-modals)
  - [Passive verbs](#passive-verbs-1)
    - [Dynamic verbs (with passive)](#dynamic-verbs-with-passive)
    - [Stative verbs (without passive)](#stative-verbs-without-passive)
    - [Idiom rule (without passive)](#idiom-rule-without-passive)
    - [Context dependent](#context-dependent)
- [Active Patterns](#active-patterns)
  - [Overview](#overview)
    - [Standard](#standard)
  - [Two objects](#two-objects)
    - [Germanic words](#germanic-words)
    - [Latin words](#latin-words)
  - [Complements (naming)](#complements-naming)
  - [Bare infinitive verbs (perception/causative)](#bare-infinitive-verbs-perceptioncausative)
  - [Continuous verbs](#continuous-verbs)
    - [Perception and discovery](#perception-and-discovery)
    - [Emotions and communication](#emotions-and-communication)
    - [Possessive and objective](#possessive-and-objective)
  - [Infinitive verbs](#infinitive-verbs)
    - [Instruction and expectation](#instruction-and-expectation)
    - [Desires and opinions](#desires-and-opinions)
    - [Phase and linking](#phase-and-linking)
    - [Intentions](#intentions)
- [Using Passive](#using-passive)
  - [In contexts](#in-contexts)
  - [Formal contexts](#formal-contexts)
    - [Factual writing](#factual-writing)
    - [Writing structure](#writing-structure)
    - [Formal speeches](#formal-speeches)
  - [Reporting](#reporting)
    - [Receiver required](#receiver-required)
    - [Receiver not required](#receiver-not-required)
    - [Revealing information](#revealing-information)

</div>

<div class="main-content">

# Linking Verbs
- When an **adjective or noun phrase** is used after a **verb** to **describe the subject or say what or who the subject is**:

  - The **adjective or noun phrase** is a **complement** 
  - The **verb** is a **linking verb**

## State of being
- Describing the **state**
  - *Be, Keep, Prove, Remain, Stay*
  
  > *- Clara **is** a doctor* 

  :warning: "Keep" is only followed by a **noun** if an **adjective follows** it

  > *- It **kept** him awake*
    
## Process of change
### Sudden/State 
- **Common verbs**  
  | Linking verb | Description | Adjectives | Example(s) |
  | --- | --- | --- | --- | 
  | **Become** | - **Formal** speeches<br> - When talking about a more<br> **abstract or technical** process. | Apparent, Aware,<br> Convinced, Infected,<br> Irrelevant, Obvious | *- I first **became** suspicious when he looked<br> into all the cars<br> - He **became** recognised as an expert.* | 
  | **Get** | - **Less formal**<br> - In **imperatives** | Difficult, Ill, Interested,<br> Pregnant, Suspicious,<br> Unhappy, Worried | *- I first **got** suspicious when he looked<br> - Don't **get** upset about it!* |
  || - In **phrases** | Get changed, Get dressed,<br> Get married/divorced | *- Where did you live before you **got married.*** |
  || - In certain **unwanted** situation | Get ill, Get old, Get tired | *- Some people **get ill** very easily.* | 
  | **Go/Turn** | - **Colour** changing | Green, Red | *- The traffic lights **turned/went** green,<br> and I pulled away.* |
  | **Go** | - **Unwanted** situation | Go deaf/blind/bald,<br> Go mad/crazy/wild,<br> Go bad/off/mouldy/rotten,<br> Go bust, Go dead,<br> Go missing, Go wrong | *- The company **went bust** and had to close.* |

- **Others**
  - *Turn out, End up*
  - *Grow, Come*
  
  :warning: "Come" and "Grow" **CAN NOT** be **followed** by a **noun phrase**

  > *When I asked him about his old friends, **he grew thoughtful** and stared out the window.*
  
### Gradual
- Use a **to-infinitive** after verbs **come, and grow.**  

  >*I eventually **came/grew to** appreciate his work.* 

## Personal guess 
### Common verbs
- **"Seeming" linking verbs**  
  - *Appear, Look, Seem, Sound, Prove*

  > *I didn't go in because she **appeared to be asleep.***

  :warning: Before **-ing verbs**, or **adjectives alive, along, asleep, and awake**, -to be is **included.** 

  > *He **seemed to be coming** downstairs.*

### Description 
- **Add** -to be
  
  >*He walked into what **seemed to be a cave***

### Opinions 
- **Omit** -to be
  
  >*She **seems** a very efficient salesperson*

# Passive Verbs 
## Active to passive


### With modals 
| Active | Example | Passive | Example (Past Participle) |
| --- | --- | --- | --- |
| **Present** | - *You **should tell** John.* | should/could/might/ought to (etc.) **be** | - *John **should be told**.* |
| **Present perfect** | - *You **should have told** John.* | should/could/ might / ought to (etc.) **have been** | - *John **should have been told**.* |
| **Present perfect continuous** | - *You **should have been telling** John while I was outside.* | should/could/might/ought to (etc.) **have been being** | - *John **should have been being told** while I was outside.* |

## Passive verbs
### Dynamic verbs (with passive)
- Describes a **direct physical action**, a **change in status**, or an **external force** acting on an object.    
  - *Carry out, Disapprove of, Hold over, Talk down to*
  - *Delay, Patronise*

  | Active | Passive | 
  | --- | --- |
  | *- Ella looked after **(V)** him **(O)**.* | *He **was looked after** (by Ella).* |

### Stative verbs (without passive)
- Describes a **state of being**, a **mental process**, or an **abstract experience.**  

  - *Take after, Come up against, Get something down*
  - *Resemble, Encounter, Write*

- **Body part and reflex**  
  Almost NEVER use the passive voice for actions that a subject **does with their own body parts** or for **involuntary sounds** 

  > *I **put out** a hand to steady myself* 

### Idiom rule (without passive)
- It is too **informal** and heavily focuses on the **specific person's personal** effort or physical body  
  
  - *Brush up on*
  - *Cast your mind back*
  - *Get something down*
  - *Take after*

  > *We **came up against** a problem*

### Context dependent 
- According to **the context**
  (With/without)
  - *Call (someone) up (order to join the army/telephone)*
  - *Call (someone) back (ask to return/telephone)*
  - *Let in (allow into a place/allow something in)*
  - *Let out (allow to leave/let out a sound)*

  | Active | Passive | 
  | --- | --- |
  | *- They put out **(V)** the fire **(O)*** | *- The fire **was put out*** |  
  | *- I put out **(V)** a hand **(O)** to steady myself* | NONE |

# Active Patterns
## Overview 
| Type | Active | Passive |
| --- | --- | --- |
| **Standard** | V + O | O + 'be' + V |
| **Germanic** | V + DO + Prep + IO | DO + 'be' + PP + (Prep) |
||| IO + 'be' + DO |
| **Latin** | V + DO + Prep + IO | DO + 'be' + PP + Prep |
| **Complement** | V + O + Complement | O + 'be' + PP + Complement |
| **Bare infinitive** | V + O + Bare infinitive | O + 'be' + To-infinitive | 
| **Continuous Verbs** | V + O + -ing | O + 'be' + PP + -ing |
|| V + -ing + O | V + being + PP + O |
|| V + N + -ing | No passive |
| **To-infinitive** | V + O + To-infinitive | O + 'be' + PP + To-infinitive |
|| V + To-infinitive + O | O + V + to be + PP<br> **(:warning: The meaning could be changed)** | 

### Standard
- Invented to answer the question: **"What happened to this object?"**
- To remove or ignore the **doer**, and to focus on the **object** by saying the direct object first.  
- :warning: **Past participles** are taken.  

| Active | Example | Passive | Example (Past Participle) |
| --- | --- | --- | --- |
| **Present simple** | - *John **tells** me that you're thinking of leaving.* | am/is/are | - *I'**m told** (by John) that you're thinking of leaving.* |
| **Past simple** | - *John **told** me that you were leaving.* | was/were | - *I **was told** (by John) that you were leaving.* |
| **Present perfect** | - *John **has told** me that you are leaving.* | have/has been | - *I **have been told** (by John) that you are leaving.* |
| **Past perfect** | - *John **had** already **told** me that you were leaving.* | had been | - *I **had** already **been told** (by John) that you were leaving.* |
| **Present continuous** | - *John **is** always **telling** me that you are leaving.* | am/is/are being | - *I **am** always **being told** (by John) that you are leaving.* |
| **Past continuous** | - *John **was** always **telling** me that you were leaving.* | was/were being | - *I **was** always **being told** (by John) that you were leaving.* |
| **Future simple** | - *I **will tell** John that you are leaving.* | will be | - *John **will be told** (by me) that you are leaving.* |
| **Future perfect** | - *By tomorrow I **will have told** John that you are leaving.* | will have been | - *By tomorrow John **will have been told** (by me) that you are leaving.* |
| **Present perfect continuous**<br> *(rare in the passive)* | - *John **has been telling** me for ages that you are leaving.* | has/have been being | - *I **have been being told** (by John) for ages that you are leaving.* |

## Two objects 
### Germanic words
- **With two passives**  
  Usually short, commonly used. 

  - *Give, Award, Hand, Lend, Offer, Send, Throw*
  - *Ask, Read, Teach*
  
  | Active | Passive |
  | --- | --- | 
  | *- Alice gave **(V)** us **(IO)** the vase **(DO)**.* | *- We **(IO)** **were given** that vase **(DO)** (by Alice).* |
  | *- Alice gave **(V)** that vase **(DO)** to **(Prep)** us **(IO)**.* | *- That vase **was given (to)** us (by Alice).* |

### Latin words
- **With one passive**  
  Usually long, used academically.  
  - *Announce, Demonstrate, Describe, Introduce, Mention, Propose, Report, Suggest*

  | Active | Passive |
  | --- | --- | 
  | *- He explained **(V)** the problem **(DO)** to **(Prep)** me **(IO)**.* | *- The problem **was explained to** me.* |

## Complements (naming)
- **Usually for verbs meaning "naming"**
  - *Appoint, Declare, Make, Nominate, Vote, Call, Name, Title*

  | Active | Passive |
  | --- | --- |
  | *- They elected **(V)** her **(O)** president **(Complement)*** | *- She **was elected** president* |


## Bare infinitive verbs (perception/causative)
- **Perception** 
  - *See, Hear, Feel, Observe, Watch, Notice*

  | Active | Passive |
  | --- | --- |
  | *- I saw **(V)** him **(O)** steal **(Bare infinitive)*** | *- He **had been seen to** steal the car.* |

- **Causative**  
  - *Make, Let, Have, Help* 

  | Active | Passive |
  | --- | --- |
  | *- The teacher made **(V)** the students **(O)** stay **(Bare infinitive)** late.* | *- The student **had been made to** stay.* | 

## Continuous verbs
### Perception and discovery 
- **Action verbs**  
  Sensory perception or discovery/action:  
  - *Hear, Notice, Observe, See*
  - *Bring, Catch, Find, Keep, Send, Show*
  
  | Active | Passive |
  | --- | --- |
  | *- They saw **(V)** the monkey **(O)** climbing **(Continuous verb)** over the fence* | *- The monkey **was seen (V) climbing (Continuous verb)** over the fence* |

### Emotions and communication
- **Stative verbs**  
  Emotion, memory and communication/avoidance 
  - *Love, Enjoy, Dislike, Hate, Like, Resent*
  - *Imagine, Remember*
  - *Avoid, Deny, Describe, Face, Report*

  | Active | Passive | 
  | --- | --- | 
  | *- I really love **(V)** people **(O)** giving **(Continuous verb)** me presents* | *- I really **love being given** presents* |

### Possessive and objective 
- **Stative verbs**  
  These are verbs **followed by a noun phrase** object and an -ing clause in the active voice. They **CANNOT** be transformed into passive sentences 

  - *Anticipate, Appreciate, Dread*
  - *Forget, Recall, Remember, Mind*
  
  > *I **dread** him finding out*

## Infinitive verbs


### Instruction and expectation 
- **Action verbs**  
  Instructing, permitting, and cognitive expectations  
  - *Advice, Allow, Instruct, Order, Tell, Ask*
  - *Feel, Mean, Understand, Require*

  | Active | Passive | 
  | --- | --- |
  | *- Mr Wang has taught **(V)** Peter **(O)** to sing **(infinitive)** for years* | *- Peter **has been taught to** sing* | 
  | *- We expect **(V1)** the government **(O1)** to propose **(infinitive)** changes **(O2)** to **(Prep)** the taxation system*| *- Changes **(O2)** to taxation system **(O1)** **are expected to be proposed*** | 

### Desires and opinions
- **Stative verbs**  
  Liking and wanting. They **DO NOT** have passive
  - *Bear, Hate, Love*
  - *Need, Prefer, Want, Wish*

  > *Susan **liked** Karl to be there*

### Phase and linking
- **Action verbs**  
  Words expressing the start, continuation, or appearance of an action
  - *Begin, Tend, Continue, Come*
  - *Appear, Seem*

  | Active | Passive |
  | --- | --- | 
  | *- Supermarkets started **(V)** to sell **(infinitive)** fresh pasta **(O)** only in the 1990s* | *-Fresh pasta **started to be sold** by supermarkets only in the 1990s.* |

### Intentions 
- **Stative verbs**  
  Words expressing effort, arrangement, or desire.   
  - *Agree, Refuse*
  - *Hope, Want*
  - *Arrange, Aim, Attempt*

  When changing to passive, **the meaning of the sentence changes.**  
  | Active | Passive |
  | --- | --- |
  | *- Petra **(O)** wanted to **(infinitive)** help **(V)** me.* | *-I **wanted to be helped** by Petra **(the meaning is shifted)**.* | 

# Using Passive 
## In contexts  
- When the **agent** is:

  - **not known**
    > *My office **was broken into** when I was on holiday*
  
  - **people in general**
    > *An order form **can be found** on page 2.*

  - **unimportant** 
    > *He **is thought to** be somewhere in Russia.*

  - **obvious**
    > *She **is being treated** in hospital*

## Formal contexts 
### Factual writing
- The **agent** is often **omitted**.  
  
  > *Nuclear waste will still be radioactive even after 20,000 years, so it **must be disposed of** very carefully.*

  Some verbs have **related nouns** which express the same meaning. These nouns can be used as the subject of the passive sentence 

  > *The **installation** of the new computer system will be completed by next month.*

### Writing structure
- In English, the **topic** is preferably placed at the **beginning** of a sentence and a **comment** on that topic at the **end**.  

  > *The three machines tested for the report contained different types of **safety valve**. **All the valves** were manufactured by the Boron Group in Germany.*

  Allows **long subjects** at the **end** of a sentence.  

  > *I **was surprised** by Dev's decision to give up his job and move to Sydney* 

  **It-clause** is normally utilized.  

  > ***It was believed** that the plan would fail*

### Formal speeches 
- To avoid any **mention of an agent**  
  
  > *The new computer system **is being installed** next month.*

## Reporting
### Receiver required  
- **Standard passive**  
  Those verbs require an **indirect object**. The action has to be received by someone.  
  - *Encourage, Persuade, Reassure, Remind, Tell, Warn, Ask, Told*
  
  | Active | Passive |
  | --- | --- | 
  | *- The security informed **(V)** us **(O)** that we have to leave* | ***We have been informed** that we have to leave* |

### Receiver not required
- **It + passive verb + that-clause**  
  Put **important information** at the **end** of the sentence 

  When the sentence start with **'there'**, the passive can also be **there + passive verb + to be/to have been**.   

  - *Allege, Believe, Calculate, Demonstrate, Reveal, Suppose*
  - *Agree, Decide, Hope, Intend, Plan (can also be followed by a to-infinitive clause)*
  - *Announce, Decide, Mention, Propose, Recommend, Suggest* 

  | Active | Passive |
  | --- | --- |
  | *- The damage is extensive, **according to** government sources* | ***- It is reported that** the damage is extensive* | 
  | *- **There are** too many obstacles to peace, **thought by** the press.* | *- **It is thought (that) there** are too many obstacles to peace*<br> *- **There are thought to be** too many obstacles to peace* | 
  >  
  
- **Subject + passive verb + to-infinitive**  
  It Makes the **subject** the **topic** of the sentence.  

  **Except** words like:

  - *Announce, Decide, Mention, Propose, Recommend, Suggest* 

  | Information at the END | Information at the FRONT |
  | --- | --- |
  | *- **It is reported that** the damage **(O)** is extensive* | *- The damage **is reported to be** extensive.* |

### Revealing information
- **It + passive verb + wh-clause**  
  To report information **given or found out**.  
  - *Reveal, Discover, Explain, Find, Know, Reveal, Show, Understand*
  
  | Active | Passive | 
  | --- | --- | 
  | *- They took **(V)** the decision **(O)** to build the bridge before they **established whether** it was actually needed.* | *- The decision to build the bridge **was taken** before **it was established** **whether** it was actually needed* |


</div>