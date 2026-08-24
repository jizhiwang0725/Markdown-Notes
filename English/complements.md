<link rel='stylesheet' href='../style.css'>

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

<div class='toc-sidebar'>

<strong>Other Files</strong>


- <a href="clause.md">Clause</a>
- <a href="communication.md">Communication</a>
- <a href="future_actions.md">Future Actions</a>
- <a href="modals.md">Modals</a>
- <a href="noun_phrase.md">Noun Phrase</a>
- <a href="passive_voice.md">Passive Voice</a>
- <a href="prepositional_phrase.md">Prepositional Phrase</a>
- <a href="tenses.md">Tenses</a>
- <a href="verb_phrase.md">Verb Phrase</a>

<strong>Table of Contents</strong>

- [Complements](#complements)
  - [Definition](#definition)
- [Subject Complements](#subject-complements)
  - [Definition](#definition-1)
  - [Noun](#noun)
    - [Rename and identify](#rename-and-identify)
  - [Adjective](#adjective)
    - [Description](#description)
  - [Verbs](#verbs)
    - [Goals and objectives](#goals-and-objectives)
    - [Future actions and plans](#future-actions-and-plans)
    - [Extra details](#extra-details)
  - [Prepositional phrase](#prepositional-phrase)
- [Object Complements](#object-complements)
  - [Definition](#definition-2)
  - [Noun](#noun-1)
    - [Rename](#rename)
  - [Adjective](#adjective-1)
    - [Causing and maintaining](#causing-and-maintaining)
    - [Mental state](#mental-state)
  - [Verbs](#verbs-1)
    - [Perception](#perception)
    - [Causative](#causative)
    - [Influence and permission](#influence-and-permission)
    - [Completed action/state](#completed-actionstate)
  - [Prepositional phrase](#prepositional-phrase-1)
    - [Judgement](#judgement)
- [Verb Complements](#verb-complements)
  - [Definition](#definition-3)
  - [Direct and indirect objects](#direct-and-indirect-objects)
    - [Future actions/states](#future-actionsstates)
    - [Experience](#experience)
    - [Thoughts and communication](#thoughts-and-communication)
    - [Phase verbs](#phase-verbs)
  - [Prepositional phrase](#prepositional-phrase-2)
- [Noun Complements](#noun-complements)
  - [Definition](#definition-4)
  - [Prepositional phrase](#prepositional-phrase-3)
  - [To infinitive](#to-infinitive)
    - [Ability and Opportunity](#ability-and-opportunity)
    - [Volition](#volition)
    - [Action and effort](#action-and-effort)
    - [Authority and obligation](#authority-and-obligation)
  - [Noun clause](#noun-clause)
    - [Communications and facts](#communications-and-facts)
- [Adjective Complements](#adjective-complements)
  - [Definition](#definition-5)
  - [Prepositional phrase](#prepositional-phrase-4)
  - [To infinitive](#to-infinitive-1)
    - [Willingness](#willingness)
    - [Emotional reaction](#emotional-reaction)
    - [Probability and certainty](#probability-and-certainty)
  - [Noun clause](#noun-clause-1)


</div>

<div class='main-content'>

# Complements
## Definition 
- A complement is a **word or clause that is LEGALLY REQUIRED by the grammar** of the sentence to complete a thought. If the complement is removed, the sentence will be broken or completely lost its sense

# Subject Complements
## Definition 
- A word or phrase that **renames, classifies, identifies or describes** the subject's **state of being quality or condition**
- It always follows a **linking word <a href="verb_phrase.md#linking"> (See more about linking verbs in verb phrase)</a>**


## Noun
### Rename and identify
- **Predicate nominative**  
  To Rename, classify, or identify the subject 
  
  | Form | Example
  | --- | --- |
  | **Phrase** | *- **The solution** is **a workaround**.<br> - **She** became **the lead developer on the project**.* | 
  | **Clause** | *- **The reality** is **that** the algorithm needs a complete rewrite*<br> *- **A sudden flat tire** is **why** they arrived late to the ceremony.* | 

## Adjective
### Description
- **Predicate adjective**  
  Describe the subject's state of being, quality, or condition 
  
  | Form | Example |
  | --- | --- |
  | **Word** |  *- **The layout** looks **responsive.***  |
  | **Phrase** | *- **The new API** seems **incredibly difficult to implement.*** | 

## Verbs
### Goals and objectives
- **To infinitive**  
  Defines what the subject aims to achieve or its intended function.
  - *Goal, objective, purpose, aim*
  
  > ***Her primary objective** is **to optimize the query performance***

### Future actions and plans
- **To infinitive**  
  Outlines a predetermined path, duty, or schedule mapped to the subject.
  - *Plan, schedule, duty, intent*

  > ***The plan** is **to migrate the database by Friday***


### Extra details  
- **Gerund**   
  > ***His primary task** is **optimizing the software***

- **To infinitive**  
  When the subject itself is a relative clause starting with "All" or "What"
  
  > ***All** you need to do is **to** start the server.*

## Prepositional phrase
| Preposition | Concept | Linking Verbs | Example |
| :--- | :--- | :--- | :--- |
| **In/Out** | State or condition | Be, Remain, Stay | *- The server is **in service*** |
| **On** | Operational status | Be, Keep | *- The system is **on standby*** |
| **Off** | Non-operational status | Be, Go | *- The secondary node is **offline*** |
| **At/In** | Condition or level | Be, Reach | *- The project is **at risk*** |
| **Under** | Process or state of being handled | Be, Go | *- The database is **under maintenance*** |  

# Object Complements
## Definition
- A word or phrase that **renames the object**, defines **how the object is judged**, or **describes the physical or mental state** the object is left in after the verb's action.

- It follows a **direct object**

## Noun
### Rename
- Verbs that relate to **naming and appointing** the new title/status of the object.  
  - *Appoint, Call, Crown, Dub, Elect, Make, Name* 
  
  > *They **elected** her **president**.*

  > *We **named** the dog **Max**.* 

## Adjective
### Causing and maintaining
-  Describes the **physical state** the object is left in after the verb's action
   - *Color, Keep, Leave, Make, Paint*  

   > *Please **keep** the door **open**.*

### Mental state 
- Describes the **mental state** the object is left in after the verb's action, and how the **subject evaluates the object**.  
  - *Find, Prove, Consider, Deem, Judge, Hold, Drive*

  > *The loud noise **drove** me **crazy**.*

## Verbs
### Perception
- **Bare infinitive**  
  Indicates a **complete action**  
  
  - *Feel, Hear, Notice, Observe, Overhear, See, Watch*
  
  > *I **saw** him **smash** the bottle.*
  
  Or the **whole action is perceived** from start to end.

  > *I **watched** him **climb** through the window, and then I called the police*

- **Continuous**   
  Suggests you perceived an **action in progress** 
  - *Feel, Hear, Notice, Observe, Overhear, See, Watch*

  > *I **saw** them **playing** football from my window.*

  Or **part of the action**

  > *I was able to **watch** them **building** the new car park from my office window*


### Causative
- **Bare infinitive**  
  These are verbs used to express that someone is **forcing, requiring, or allow someone else to do something**
  
  - *Make, Let, Have*

  > *His exam results might **make** him **work** harder.*

  > *I **had** the mechanic **fix** my brakes*

### Influence and permission
- **To infinitive**  
  These verbs naturally involve interacting with another person to **make, allow, or ask them to do something.**  
  - *Advise, Allow, Believe, Cause, Command, Enable, Encourage, Entitle*
  - *Force, Invite, Order, Persuade, Remind, Show, Teach, Tell*

  > *The police **warned** everyone **to stay** inside with their windows closed.*

### Completed action/state
- **Past participle**
  - *Get, Have, Keep, Like, Need, Prefer, Want* 
  
  > *I **need** this report **finished** by tomorrow.*
  
  > *She **had** her car **washed**.*

## Prepositional phrase
### Judgement
- **As/to be**  
  Define how the object is **viewed or judged**  
  - *Accept, Define, Describe, Recognise, Regard, Treat, View* 
  - *Assume, Believe, Consider, Declare, Find, Judge, Prove*

  > *They **regard** him **as a genius**.*

  > *Economists **believe** the opposite **(to be) true***.

  > *Please **use** this rolled-up towel **as** a pillow.*

# Verb Complements 
## Definition
- It completes the verb's logic.  

## Direct and indirect objects
- Transitive verbs require **objects** to complete their action 
  Objects need to have the **properties of nouns.** 

### Future actions/states 
- **To infinitive**  
  These verbs describe **internal thoughts, personal commitments or individual capabilities.**  
   - *Agree, Consent, Fail, Hope, Manage, Offer, Pretend, Refuse, Start, Threaten, Volunteer* 
  
  > *They decided **to refactor the entire module.*** 

  > *They **threatened to kill** him* 

  Express strong **preferences or wants** 
  - *Love, Hate, Need, Prefer, Want, Wish, Bear*
  
  > *I **want to buy** a car*

  Verbs dealing with what someone anticipates will happen 
  - *Expect, Mean, Arrange, Aim*
  
  > *We **expect to win** the game.*

### Experience 
- **Gerunds**  
  Verbs involving experience, stopping, or starting

  > *We must avoid **hardcoding the credentials***

  **Having + past participle**  
  - *Admit, Deny, Forget, Recall, Regret, Remember*
  
  > *I now **regret having bought** the car.*  

### Thoughts and communication 
- **wh-/that - clause**
  To express a **complex idea**

  > *I don't understand **why the loop is failing*** 

### Phase verbs 
- **To infinitive**
  These verbs describe the **beginning, middle or end of an action.**
  - *Start, Begin, Continue, Cease*

  > *Supermarket **started to sell** fresh pasta*

## Prepositional phrase 
- **Dependent prepositions**  
  Some verbs are hardwired to require a prepositional phrase to finish their thoughts 

  A direct object can sometimes be added between the prepositional phrase and the head verb.  

  | Preposition | Concept | Verb | Example |
  | :--- | :--- | :--- | :--- |
  | **Of** | Content & origin | Approve, Hear, Know, Speak, Talk, Tell | *Have you ever **heard of** (anyone) getting arrested for gossiping before?* |
  | **From** | Separation & barrier | Deter, Discourage, Keep, Prevent, Prohibit, Stop | *The noise from next door **prevented** me **from** sleeping.* |
  | **To** | Reactions & transfers | Adapt, Adjust, Admit, Look forward, Own up | *She **confessed to stealing** the money.*<br>*Can you **pass** that bandage **to** me?*<br>*She **announced** her decision **to** the public.* |
  | **At** | Specific aim | Look, Stare, Point, Shout, Smile, Marvel, Guess, Arrive, Stop | *I **smiled at** him.* |
  | **For** | Purpose & beneficiary | Collect, Mend, Repair | *I **built** a doll's house **for** my daughter.*<br>*He **fixed** the tap **for** me.* |
  | **With** | Friction & collisions | Agree, Connect, Sympathize, Argue, Fight, Collide | *I strongly **agree with** your assessment.*<br>***Compare** some recent work **with** your older stuff, and you'll see how much you've improved.* |
  | **On** | Dependency & impact | Focus, Concentrate, Deliberate, Rest, Insist, Intrude, Depend, Rely | *They **based** the new movie **on** a true story.*<br>*Newspaper editors are being urged not to **intrude on** the grief of the families of missing servicemen.* |
  | **In** | Immersion & state | Believe, Trust, Confide, Participate, Engage, Result, Culminate, Major | *Don't **involve** me **in** your argument.*<br>*Their many years of research have finally **culminated in** a cure for the disease.* |
  | **As** | Roles | Work, Speak, Use | *I **work as** a software engineer* |
  | **By** | Mechanisms | Begin, Close, End, Finish (off/up), Open, Start (off/out) | *Can you **begin by** cleaning the floor?* |

  **<a href="prepositional_phrase.md#dependent-prepositions">(See more about dependent prepositions in prepositional phrase)</a>**




# Noun Complements 
## Definition 
- A phrase or clause that immediately follows a noun to complete its meaning. 
- Defining what the noun actually is, often expanding on **abstract concepts**

## Prepositional phrase
| Preposition | Concept | Nouns | Example |
| :--- | :--- | :--- | :--- |
| **Of** | Content & origin | Cause, Advantage, Disadvantage, Lack, Understanding, Example, Proof, Habit | *The main **advantage of** this framework is its speed* |
| **To** | Reactions & transfers | Solution, Reaction, Reply, Response, Approach, Threat, Damage, Answer, Alternative | *They finally found a **solution to** the memory leak* |
| **For** | Purpose & beneficiary | Need, Demand, Reason, Preference, Reputation, Responsibility | *There is a high **demand for** efficient algorithms* |
| **With** | Friction & collisions | Relationship, Connection, Difficulty, Trouble, Sympathy | *The developer had no **difficulty with** the syntax* |
| **On** | Dependency & impact | Effect, Impact, Influence, Attack, Dependence, Reliance | *The update had a negative **impact on** the server's performance.* |
| **Between** | Distinctions | Difference, Comparison, Connection, Relationship, Contrast | *The **difference between** the two variables is negligible* |
| **In** | Immersion & state | Increase, Decrease, Rise, Fall, Interest, Experience, Belief, Delay | *We saw a massive **increase in** network traffic* |

## To infinitive
### Ability and Opportunity
- Nouns that define whether the subject has the **skill or the chance to perform an action**
  - *Ability, Inability, Capacity, Chance, Opportunity*
  
  > *The hardware lacks the **capacity to run** the reinforcement learning model*

### Volition 
- Nouns that express what someone **wants, intends, or is willing to do**
  - *Desire, Wish, Intention, Willingness, Reluctance, Eagerness, Ambition, Determination*
  
  > *Her **determination to master** Java paid off*

### Action and effort
- Nouns that represent the **physical or mental attempt** to do something, or the choice made regarding an action 
  - *Attempt, Effort, Failure, Struggle, Decision, Refusal*

  > *His **failure to compile** the code caused a delay*

### Authority and obligation 
- Nouns that deal with **rules, permission, and necessities**
  - *Permission, Right, Authority, Obligation, Need, Requirement*

  > *You do not have **permission to access** the root directory*

## Noun clause
### Communications and facts  
- Used heavily with nouns related to **communication, cognition and facts**
  Often **that-clause**. It defines exactly what the noun is, the word "that" is just a conjunction joining the clauses 
  - *Fact, Belief, Idea, Rumour, Assumption, Claim, Thought, Realization*

  >*The **rumour that** the project was canceled is true.*

# Adjective Complements 
## Definition 
- Immediately follows an adjective and is required to complete its meaning.  

## Prepositional phrase
| Preposition | Concept | Adjectives | Example |
| :--- | :--- | :--- | :--- |
| **Of** | Content & origin | Afraid, Aware, Fond, Sure, Tired, Worthy | *He threw a party **worthy of** a millionaire* |
| **To** | Reactions & transfers | Similar, Prior, Equivalent, Accustomed, Opposed, Prone, Immune | *I've always been **prone to** headaches* |
| **For** | Purpose & beneficiary | Ready, Eligible, Fit, Notorious, Famous, Responsible | *The company is **notorious for** paying its bill late.* |
| **With** | Friction & collisions | Angry, Obsessed, Okay, Satisfied, Familiar, Involved, Associated | *As a doctor, you should not become too emotionally **involved with** the children in your care* |

## To infinitive
### Willingness 
- Adjectives that describe whether the subject is **prepared or willing** to perform the action 
  - *Able, Ready, Prepared, Reluctant, Eager, Willing*
  - *Unable, Unwilling, Hesitant, Anxious*

  >*The user was **hesitant to grant** admin privileges*

### Emotional reaction 
- Adjectives that express a feeling or attitude that is directly **caused by**, or **directed toward** the **action in the infinitive**
  - *Happy, Sad, Glad, Relieved, Surprised*
  
  > *She was **surprised to find** a logic error in the core loop.*

### Probability and certainty
- Adjectives that evaluate **how likely an action is to happen.**  
  - *Likely, Unlikely, Certain, Bound, Liable*

  > *The legacy system is **bound to fail** eventually*

## Noun clause
- Often a that-clause
  
  > *I am certain **that** the syntax is correct*



</div>