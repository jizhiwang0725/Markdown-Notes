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
- <a href="future_actions.md">Future Actions</a>
- <a href="modals.md">Modals</a>
- <a href="noun_phrase.md">Noun Phrase</a>
- <a href="passive_voice.md">Passive Voice</a>
- <a href="prepositional_phrase.md">Prepositional Phrase</a>
- <a href="tenses.md">Tenses</a>
- <a href="verb_phrase.md">Verb Phrase</a>

<strong>Table of Contents</strong>

- [Dependent Clause](#dependent-clause)
  - [Types of dependent clauses](#types-of-dependent-clauses)
- [(Adjective) Relative Clause](#adjective-relative-clause)
  - [Defining and non-defining](#defining-and-non-defining)
    - [Definition](#definition)
    - [For additional information](#for-additional-information)
    - [Possession](#possession)
    - [Preposition "of"](#preposition-of)
    - [Quantity rule](#quantity-rule)
    - [Relative word omission](#relative-word-omission)
  - [Nominal](#nominal)
    - [Definition](#definition-1)
    - [Unknown and indefinite](#unknown-and-indefinite)
- [(Adverb) Time Clause](#adverb-time-clause)
  - [Time conjunctions](#time-conjunctions)
  - [Since](#since)
  - [Present simple refers to the future](#present-simple-refers-to-the-future)
  - [Reduced time clauses](#reduced-time-clauses)
- [(Adverb) Conditional Clause](#adverb-conditional-clause)
  - [Conditional conjunctions](#conditional-conjunctions)
  - [Zero conditional](#zero-conditional)
    - [Predicates](#predicates)
    - [Past habits](#past-habits)
  - [First conditional](#first-conditional)
    - [Likely future scenarios](#likely-future-scenarios)
    - [Want to achieve something in the future](#want-to-achieve-something-in-the-future)
  - [Second conditional](#second-conditional)
    - [Unlikely or imaginary scenarios](#unlikely-or-imaginary-scenarios)
  - [Third conditional](#third-conditional)
    - [Impossible past scenarios](#impossible-past-scenarios)
  - [Relevance conditional](#relevance-conditional)

</div>

<div class="main-content">


# Dependent Clause 
## Types of dependent clauses 
- **Noun clause**  
  Act as a noun 

- **Adjective clause**  
  Act as an adjective to modify a noun or pronoun 

- **Adverb clause**  
  Acts as an adverb to modify a verb
  Answers how, when, where or why. 

# (Adjective) Relative Clause
## Defining and non-defining
### Definition  
- **Defining** 
  - Gives **essential information** that **specifies or identifies** among which person, place, or thing you are talking about.  
  - No comma.  

- **Non-defining** 
  - They act like a **parenthetical aside**, adding **bonus details to a noun we already recognize**
  - Relative pronouns must be included
  - With comma

### For additional information
- **About things**
  | Relative Words | Usage | Example(s) |
  | :--- | :--- | :--- |
  | **That** | - After specific pronouns<br> (Something, Anything, All, Little, Much, None)<br> - Used in **informal context** | *- These walls are **all that** remain of the city*<br> *- Decorating is a job **(that)** I hate most* |
  | **Which** | - Used in **formal** contexts | *- This is the drawing **(which)** I like the most* |

- **About people**
  | Relative Words | Usage | Example(s) |
  | :--- | :--- | :--- |
  | **That**<br> (Defining clauses) | - Used in **informal** contexts<br>- **Cannot** follow a **preposition**,<br> the preposition is usually **at the back** | - *The boy **(that)** Elena had shouted at smiled (passive)*<br> *- The office **that** Juan took us **to** was filled with books* |
  | **Who** | - Used in **formal** contexts<br> - **Cannot** follow a **preposition**,<br> the preposition is usually **at the back** | *- He is the man **(who)** I met at Aisha's party*<br> *- He is the men **who** was in the party*<br> *- The playground wasn't used by the children **who** it was built **for*** |
  | **Whom** | - Used in **formal** contexts **as an object**<br> - **Preposition** is usually **at the front**<br> | *- The boy **(whom)** Elena had shouted at smiled (passive)*<br> *- Professor Johnson, **whom** I have long admired,<br> is to visit the university next week*<br> *- There are 80 teachers in the Physics department,<br> **among whom** are 24 professors* |

- **About events**
  | Relative Words | "Which" Equivalent | Usage | Example |
  | --- | --- | --- | --- |
  | **When** | **At/On/By which** | - Referring to time | *- The camera records the time **when/at which** the photo is taken* |
  | **Whereby** | **On/By which** | - Method or means | *- We need to develop a system **whereby/in/by which** workers<br> and management can communicate more effectively* |
  | **Where** | **At/In which** | - Location |*- This was the place **where/at/in which** we first met* |

### Possession 
- **Whose + noun**  
  In written English, when we talk about something belonging to or associated with a **person, animal or plant** 

  > *Stevenson is an architect **whose designs** have won international praise*  

  In academic writing, it is used to talk about a wide variety of **'belonging to' relationships** 

  > *Students have to solve problem **whose solutions** require a knowledge of calculus*
  
  Talk about **towns, countries, or organisations** 

  > *The film was made in Botswana, **whose wildlife parks** are larger than those in Kenya*

  **"Whose"** can come **after a preposition**. Putting the preposition at the **end** of the clause is more **natural in informal and spoken English**

  > *I now turn to Freud, **from whose** work the following quotation is taken (**whose** work the following quotation is taken **from**)*

- **Noun + of which**  
  A formal substitution

  > *A huge amount of oil was spilled, **the effects of which** are still being felt.*


### Preposition "of"
- **That/which ... of**  
  Used in **less formal** contexts 

  > *The school **(that/which)** she is head **of** is closing*

- **Noun + of which**  
  A formal substitution 

  > ***The school of which** she is head is closed* 

### Quantity rule 
- **Of which/whom**  
  When describing a portion or quantity of a large group 
  - *All, Each, Many, Most, Neither, None, Part, Some, A number and superlative*
  
  > *Lotta was able to switch between German and Russian, **both of which** she spoke fluently*
  
### Relative word omission
- **CAN omit**  
  - If it acts as the **object** in a defining relative clause 

- **CANNOT omit**  
  - If it acts as the **subject** in a defining relative clause 
  - It is in a **non-defining relative clause**
  - When a **preposition** is **present**. 

## Nominal
### Definition 
- Used like a **noun phrase** in a sentence 

### Unknown and indefinite 
| Pronoun | Usage | Example | 
| --- | --- | --- |
| **What** | - The **thing** | *- I didn't know **what** I should do next* |
| **Who** | - The **people** | *- Can you give me a list of **who** has been invited* | 
| **Whatever** | - **Anything** or it doesn't matter what | *- I'm sure I'll enjoy eating **whatever** you cook* |
| **Whichever** | - **One** thing or person from a limited number | *- **Whichever** one of you broke the window will have to pay for it* |
| **Whoever** | - The **person/group** who or any **person/group who** | *- **Whoever** wins will go on to play Barcelona in the final* 

# (Adverb) Time Clause
## Time conjunctions  
| Conjunction | Meaning | 
| --- | ---
| When | Specific point in time
| While/As | Two actions happening at the exact same time |
| Before/After | The sequence of two events | 
| As soon as/Once | One event happens immediately following another | 
| Until/Till | An action continues up to a specific point in<br > time and then stops |
| Since | An action started at a specific point in the past<br> and continues to the present
| By the time | One action is completed earlier than a second<br> action

## Since 
- **Past simple** verb in the **time clause**, and a **present perfect** verb in the **main clause**. 
  
  > *Since Mr Dodson **became** president unemployment **has increased**.*

- When two situations in the main clause and time clause **extend until the present**, use **present perfect** for both.  
  
  > ***Have** you **met** any of your neighbours since you **have lived** here?*

## Present simple refers to the future
- Use **future tense** for the **main clause** to indicate it is a future event, and use **present tense** for **time clause**.

  > *I **will** call you when I **get** home*

## Reduced time clauses 
- When the subject of the time clause and the subject of the main clause are **exactly the same person or thing**, you can sometimes "reduce" the **time clause** by **dropping the subject** and changing the **verb** in to an **-ing participle**. 

  > *Before **you sign** the contract, you should read it carefully.*  
  *Before **signing** the contract, you should read it carefully.*  

# (Adverb) Conditional Clause
## Conditional conjunctions
- **All-rounders**
  | Conjunctions | Meaning |
  | --- | --- |
  | (What) if | The **standard condition** |
  | Even if | The result stays the **same regardless of the condition** | 
  | Whether... or not | Introduces **two alternative** conditions that lead to the **same** result | 

- **Real & likely (zero & first conditional)**
  | Conjunctions | Meaning |
  | --- | --- | 
  | Provided/Providing (that) | "On the **strict condition** that"<br> (more formal than as long as) |
  | As long as | "Only if". Sets a **strict limit or boundary** |
  | In case | As a **precaution** against a possible future event | 
  | Assuming/Assume (that) | Accepting something **as most likely to true** to establish a condition |

  > *(First) I will lend you the car **as long as** you **fill** the tank.* 


- **Hypothetical conjunctions (second & third conditional)**
  | Conjunction | Meaning |
  | --- | --- | 
  | Supposing/Suppose/Imagine (that) | Discussing a **hypothetical condition** | 

  > *(Second) **Imagine** you **could** live anywhere, where would you go*

  > *(Third) **Suppose** you **had missed** that flight, what would you have done?*

- **First & second conditional**
  | Conjunction | Meaning |
  | --- | --- | 
  | Unless | "If not" or "expect if" (the clause follows it should be **POSITIVE**) |

  > *(First) I won't **go unless** you pay.*  
  (Real limits)

  > *(Second) I **wouldn't ask** for your help unless I really needed it.*  
  (Imaginary boundaries in the present)

## Zero conditional
### Predicates
- **Present simple**  
  Used as a **predicate** for general truths or facts.    

  > ***If** you heat ice, it melts.*

### Past habits
- **Past simple**  
  Used to set up a certain **condition** in the past. Often used to describe past habits.    

  > ***If** the weather **was nice**, we usually ate dinner outside*

## First conditional 
### Likely future scenarios
- **Present tense**  
  When we say that something (often something **negative**) **is conditional on something else**
  
  > ***You'll/You are going to** knock that glass over **if** you're not careful.*

  When one thing is the **logical consequence of another** and is likely to happen.  

  > ***If** you don't switch on the monitor first, the computer **won't** come on.*

  > ***Assuming** the train **is on time**, we will be in London by noon.*
  
  > ***If** Erik phones, **I'll** let you know.*

### Want to achieve something in the future
- **Be to + infinitive in if-clause**  
  To say that something must **happen first** (in the **main clause**) before something **else can happen** (in the **if-clause**)

  > *If the human race **is to survive**, we must look at environmental problems now.*
  
## Second conditional 
### Unlikely or imaginary scenarios
- **Past simple**

  > ***Suppose** she **asked** you, what would you say?*

## Third conditional 
### Impossible past scenarios
- **Past perfect**  
  The action is finished, you can't go back

  > ***Suppose** **she had asked** you, what would you have said?*
 
## Relevance conditional 
- **Be going to**  
  Future event does NOT depend on the action described. The condition just **explains why the speaker is bringing it up**.  
  
  > ***I'm going to open** a bottle of lemonade, **if** you want some.*

</div>


