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
- <a href="future_actions.md">Future Actions</a> 
- <a href="modals.md"> Modals </a>
- <a href="passive.md">Passive Sentences</a>  
- <a href="tenses.md">Tenses</a>

<strong>Table of Contents</strong>

- [(Adverbial) Time clauses](#adverbial-time-clauses)
  - [Common time conjunctions](#common-time-conjunctions)
  - [Since](#since)
  - [Present simple refers to the future](#present-simple-refers-to-the-future)
  - [Reduced time clauses](#reduced-time-clauses)
- [(Adverbial) Conditional clauses](#adverbial-conditional-clauses)
  - [Common conditional conjunctions](#common-conditional-conjunctions)
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

# (Adverbial) Time clauses
## Common time conjunctions  
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

# (Adverbial) Conditional clauses
## Common conditional conjunctions
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


