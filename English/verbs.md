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
- <a href="passive_voice.md">Passive Voice</a>
- <a href="prepositions.md">Prepositions</a>
- <a href="tenses.md">Tenses</a>

<strong>Table of Contents</strong>

- [Transitive verbs](#transitive-verbs)
  - [Monotransitive verbs](#monotransitive-verbs)
    - [V + DO](#v--do)
  - [Ditransitive verbs](#ditransitive-verbs)
    - [V + IO + DO](#v--io--do)
    - [V + DO + prep + IO](#v--do--prep--io)
  - [Complex transitive verbs](#complex-transitive-verbs)
    - [V + DO + object complement](#v--do--object-complement)
  - [Transitive prepositional verbs](#transitive-prepositional-verbs)
    - [V + DO + prepositional phrase](#v--do--prepositional-phrase)
- [Intransitive verbs](#intransitive-verbs)
  - [Unergative verbs](#unergative-verbs)
  - [Unaccusative verbs](#unaccusative-verbs)
  - [Linking Verbs](#linking-verbs)
    - [V + subject complement](#v--subject-complement)
  - [Intransitive prepositional verb](#intransitive-prepositional-verb)
    - [V + preposition phrase](#v--preposition-phrase)
- [Ambitransitive verbs](#ambitransitive-verbs)
  - [Transitive/Intransitive verbs](#transitiveintransitive-verbs)
- [Modals](#modals)
  - [Pure modals](#pure-modals)
    - [Features](#features)
    - [Past tense](#past-tense)
  - [Semi-modals](#semi-modals)
    - [Dual meaning](#dual-meaning)
    - [Common semi-modals](#common-semi-modals)
  - [Common question patterns](#common-question-patterns)
- [(Modals) Capability \& Permission](#modals-capability--permission)
  - [General abilities](#general-abilities)
    - [In action (can)](#in-action-can)
    - [Capability (can/be able to)](#capability-canbe-able-to)
    - [Senses or feelings (can)](#senses-or-feelings-can)
    - [Passive voice (can)](#passive-voice-can)
  - [Past abilities](#past-abilities)
    - [Single past achievement (be able to)](#single-past-achievement-be-able-to)
    - [General past abilities (could)](#general-past-abilities-could)
    - [Negative past achievements (couldn't/wasn't able to)](#negative-past-achievements-couldntwasnt-able-to)
  - [Permission](#permission)
    - [General actions (can/be allowed to)](#general-actions-canbe-allowed-to)
    - [Particular actions (be allowed to)](#particular-actions-be-allowed-to)
    - [Prohibitions (can't/be not allowed)](#prohibitions-cantbe-not-allowed)
- [(Modals) Degree of Certainty \& Deductions](#modals-degree-of-certainty--deductions)
  - [Degrees of certainty](#degrees-of-certainty)
    - [General truth (can)](#general-truth-can)
    - [Theoretical possibilities (could)](#theoretical-possibilities-could)
    - [Expectation (should/ought to)](#expectation-shouldought-to)
    - [Possible (may/might/could (have))](#possible-maymightcould-have)
    - [Impossible (can't/couldn't)](#impossible-cantcouldnt)
  - [Logical deductions](#logical-deductions)
    - [Strong deductions (must have)](#strong-deductions-must-have)
    - [Present events (must be/have (got) to be)](#present-events-must-behave-got-to-be)
    - [Future (must be going)](#future-must-be-going)
- [(Modals) Habits \& Truth](#modals-habits--truth)
  - [General truths and habits](#general-truths-and-habits)
    - [General behaviour or habits (will)](#general-behaviour-or-habits-will)
    - [Facts (will)](#facts-will)
    - [Non-essential criteria (needn't/don't have to)](#non-essential-criteria-needntdont-have-to)
    - [Criticism in speech (will)](#criticism-in-speech-will)
  - [Past events/situations](#past-eventssituations)
    - [Clear time reference (would/used to)](#clear-time-reference-wouldused-to)
    - [Without clear time reference (used to)](#without-clear-time-reference-used-to)
    - [The imagined past (would have)](#the-imagined-past-would-have)
    - [The assumed past (will have)](#the-assumed-past-will-have)
- [(Modals) Obligation, Advice \& Reaction](#modals-obligation-advice--reaction)
  - [Formal rules and warnings (must/must not)](#formal-rules-and-warnings-mustmust-not)
  - [Obligation](#obligation)
    - [Inferred obligations (must have to)](#inferred-obligations-must-have-to)
    - [External obligations (have (got) to)](#external-obligations-have-got-to)
    - [Lack of obligation (not have to)](#lack-of-obligation-not-have-to)
  - [Necessity](#necessity)
    - [Practical or internal necessity (need/need to)](#practical-or-internal-necessity-needneed-to)
    - [General necessity (need to)](#general-necessity-need-to)
    - [Lack of necessity (needn't/not need to)](#lack-of-necessity-needntnot-need-to)
  - [Recommendations](#recommendations)
    - [General comments (should/ought to)](#general-comments-shouldought-to)
    - [Present, specific comments (had better)](#present-specific-comments-had-better)
  - [Reaction to past events](#reaction-to-past-events)
    - [Expressing regret (should/ought to have)](#expressing-regret-shouldought-to-have)
    - [Expressing criticism (shouldn't/oughtn't to have)](#expressing-criticism-shouldntoughtnt-to-have)
- [Advanced Syntactic Patterns](#advanced-syntactic-patterns)
  - [Compensation](#compensation)

</div>

<div class="main-content">


# Transitive verbs
## Monotransitive verbs
### V + DO
- Follow by a **direct object**
  An action that happens **to** something or someone.   
  It requires a **direct object**, otherwise the sentence **feels incomplete**.  
  - *Drink, Chase, Hunt*

  > *She **closed** the **door.***
  
  Direct object is **NOT required** when it is clear from the **context**
  - *Sing, Answer, Ask, Cook, Dance, Read, Smoke, Study, Wash, Wash up, Wave, Win*

  > *She **plays** (the saxophone) beautifully.*

## Ditransitive verbs
### V + IO + DO
- The indirect object goes **before** the direct object
  > *Can you **bring** me **(IO)** some milk **(DO)** from the shop?* 

- Preposition **can NOT be added** to verbs that describe an **abstract concept**
  - *Allow, Ask, Cost, Deny, Forgive, Guarantee, Permit, Refuse* 

  > *We all **envied** him his lifestyle.* 

### V + DO + prep + IO 
- As **an alternative** to the first structure
  > *Can you **bring** some milk **(DO)** to me **(IO)** from the shop?*

  To **focus particular attention** on the object after to/for
  > *Give your documents to **the reception**.*

  When the IO is a **lot longer** than the DO: 
  > *Jasmin taught music to **a large number of children at the school**.*

  If the DO is a **pronoun**: 
  > *- I gave **them** to Isa.*

  | Preposition | Core meaning / use case | Verbs | Examples |
  | --- | --- | --- | --- | 
  | **To** | - **Transfer**, direction, or communication.<br> - Action requires a **recipient**<br> to actively receive it. | Give, Send, Hand, Pass,<br> Show, Teach, Tell, Sell,<br> Lend, Offer, Bring | *- I **handed** him the shiny new access keys today.*<br> *- I **handed** the shiny new access keys **to** him.* |
  | **For** | - **Benefaction**, creation, or doing a favor.<br> - Action can be done **alone**;<br> recipient benefits later. | Buy, Make, Build, Get,<br> Find, Cook, Save, Order,<br> Write, Leave | *- She **cooked** us a large, delicious, and healthy dinner.*<br> *- She **cooked** a large, delicious, healthy dinner **for** us.* |
  | **Of** | - **Inquiry** or expectation.<br> - Asking for information or<br> **requiring** something from someone. | Ask, Require, Demand,<br> Expect, Beg | *- Can I **ask** you a very important favor today?*<br> *- Can I **ask** a very important favor **of** you?* |

## Complex transitive verbs
### V + DO + object complement
- Some verbs requires an **object complement** to make the sentence complete 

  **<a href="complements.md">See in note about complements</a>**

## Transitive prepositional verbs 
### V + DO + prepositional phrase
- Some verbs requires a **preposition** and its corresponding **prepositional object**

  **<a href="prepositions.md">See in note about prepositions</a>**

# Intransitive verbs
## Unergative verbs 
- The subject is the **agent**. 
  The subject is actively willfully and consciously **performing the action** 
  - *Run, Swim, Sing, Jump, Work, Talk, Laugh, Sneeze*

  > *The developer **laughed***

## Unaccusative verbs
- The action is **happening to the subject**, or the subject is experiencing a change of state, condition or location 
  - *Fall, Die, Melt, Arrive, Disappear, Emerge, OCcur, Collapse*
  
  > *THe ice **melted***

## Linking Verbs
### V + subject complement
- **Describing the state**
  - *Be, Keep, Prove, Remain, Stay*
  
  > *- Clara **is** a doctor.* 
    
- **Sudden/State changes**  
  | Linking verb | Description | Adjectives | Examples |
  | --- | --- | --- | --- | 
  | **Become** | - **Formal** speeches<br> - When talking about a more<br> **abstract or technical** process. | Apparent, Aware, Convinced,<br> Infected, Irrelevant, Obvious | *- I first **became** suspicious when he looked around*<br> *into all the parked cars on the busy street.*<br> *- He quickly **became** recognised as a technical expert.* | 
  | **Get** | - **Less formal**<br> - In **imperatives**<br> - Emphasize a **sudden/unexpected event** | Difficult, Ill, Interested,<br> Pregnant, Suspicious, Unhappy,<br> Worried | *- I first **got** extremely suspicious when he looked away.*<br> *- Please do not **get** so upset about it today!*<br> *- He sadly **got bitten** by the angry stray dog.* |
  | | - In **phrases** | Get Changed, Get Dressed,<br> Get Married, Get Divorced | *- Where exactly did you live before you **got married**?* |
  | | - In certain **unwanted** situations | Get Ill, Get Old,<br> Get Tired | *- Some young people unfortunately **get ill** very easily nowadays.* | 
  | **Go/Turn** | - **Colour** changing | Green, Red, Blue,<br> Dark, Pale, Yellow | *- The traffic lights quickly **turned** green right away,*<br> *and I safely pulled away from the busy intersection.* |
  | **Go** | - **Unwanted** situation | Deaf, Blind, Bald,<br> Mad, Crazy, Wild,<br> Bad, Off, Mouldy,<br> Rotten, Bust, Dead,<br> Missing, Wrong | *- The small local tech company **went bust** last week.*<br> *- He quickly noticed the milk **went bad** this morning.* | 
  | **Turn Out** | - **Final result**<br> - Often unexpected or after<br> a long sequential process. | Fine, Right, Well,<br> Badly, True, Perfect | *- The highly complicated software project **turned out** fine ultimately.*<br> *- His totally crazy prediction actually **turned out** perfectly true.* |
  | **End Up** | - **Final state**<br> - Reaching a situation after<br> a long series of events. | Alone, Homeless, Rich,<br> Dead, Broken, Lost | *- He did not want to **end up** totally alone.*<br> *- The heavy lost package **ended up** completely ruined today.* |
  | **Grow** | - **Gradual change**<br> - Developing slowly over a<br> specific period of time. | Old, Dark, Cold,<br> Impatient, Tired, Accustomed | *- The developer slowly **grew** accustomed to the Python syntax.*<br> *- The weather suddenly **grew** very cold and quite dark.* |
  | **Come** | - **Positive realization**<br> - Evolving into a new<br> physical or mental state. | True, Alive, Loose,<br> Untied, Right, Awake | *- His childhood dream to travel finally **came** entirely true.*<br> *- The tight rope slowly **came** loose in the wind.* |

  :warning: "Come" and "Grow" **CAN NOT** be **followed** by a **noun phrase**
  
- **Gradual changes**  
  - *Come/Grow to*

  >*I eventually **came/grew to** appreciate his work.* 

- **Personal Guesses**  
  These verbs are used to express an **observation or assumption**. 
  - *Appear, Look, Seem, Sound, Prove*

  | Usage | Context / use case | Trigger words | Examples |
  | --- | --- | --- | --- |
  | **Include "to be"** | - **Objective descriptions**<br> When describing a factual state<br> or physical object. || *- He walked into what seemed **to be** a cave.* |
  || - **Before continuous verbs**<br> When connecting the linking verb<br> to an ongoing action. | Continuous (-ing) verbs | *- He seemed **to be** coming downstairs right now.* |
  || - **Before specific adjectives**<br> Specifically before the condition<br> adjectives listed. | Alive, Along, Asleep, Awake | *- I did not go inside today because she*<br> *appeared **to be** asleep on the comfortable couch.* |
  | **Omit "to be"** | - **Subjective opinions**<br> When stating a personal evaluation<br> or a judgement. || *- She seems a very efficient and capable salesperson.* |
  || - **Without an object**<br> Actions that are purely<br> reflexive in nature. | Sleep, Run, Fly | *- The small blue bird quickly flew far away.* |

## Intransitive prepositional verb  
### V + preposition phrase
- Some verbs are **followed straight by a preposition**.  

  **<a href="prepositions.md">See in note about prepositions</a>**

# Ambitransitive verbs 
## Transitive/Intransitive verbs
- **Words that can be either transitive or intransitive.**  
  Words that relate to a **change**   
  - *Bring, Bend, Break, Increase, Move, Open, Shut, Start, Vary, Weaken*
  
  > *She **closed** the door. (transitive)*  

  > *The door **closed**. (intransitive)*  


# Modals
## Pure modals
### Features
| Features | Common words |
| --- | --- |
| - **No "s"** in the third-person singular.<br> - Followed by a **bare verb.**<br> - Direct **questions and negation**.<br> - **NO -ing, -ed, or to** forms | *Can, Will, Would, Shall,<br> Should, May, Might, Must* 

### Past tense 
| Modal | Past Tense |
| --- | --- |
| Can | Could |
| Will | Would 
| May | Might |
| Must | Had to | 

## Semi-modals
### Dual meaning
| Usage | Grammatical Features | Example(s) |
| :--- | :--- | :--- |
| **As verbs**<br> (Common and informal) | - Normally used in **affirmative sentences.**<br> - Uses **"do/does."** <br> - Takes **infinitive** if next word is a verb. | - *She **doesn't dare** to look.* <br> - *He **needs to** worry.* |
| **As modals**<br> (Formal) | - Normally used in **negative sentences**<br> or with **negative words**.<br> (e.g., *Hardly, Never, Nobody*) | - *The changes **need only** be small to<br> make the proposals acceptable.* |

### Common semi-modals
- **Core** 
  - *Need*
  - *Dare*
  - *Used to*
  - *Ought to*

- **Phrasal**     
  - *Have (got) to*
  - *Be able to*
  - *Be going to*
  - *Be supposed to*
  - *Had better*

## Common question patterns
| Purpose | Modal(s) | Context / Usage | Example(s) |
| :--- | :--- | :--- | :--- |
| **Possibility** | Could/Can/Be likely | - **Informal**, daily settings<br> | - ***Could** it be that you don't want to leave?*<br> - ***Are** you **likely** to be in Spain again this summer?* |
|| Might | - **Formal** | - ***Might** they be persuaded to change their mind?* |
| **Ability** | Can | - **General** ability. | - ***Can** you speak Russian?* |
| **Permission** | May | - **Formally** asking for **permission** and<br> offering help | - ***May** I help you?* |
| **Necessity** | Have | - Hope for or expect a **negative answer.** | - ***Do** we **have** to answer all the questions?* |
| **Advice<br> Confirmation** | Should/Shall/Had better | - Seeking **advice or confirmation.** | - ***Should/Shall** I phone for a taxi for you?*<br> - ***Had** we **better** get a taxi?* |

# (Modals) Capability & Permission
## General abilities 
### In action (can)
- **Can**  
  When talking about something that **is happening as we speak**
  - *The only thing/place/time*
  - *All (means the only thing)*

  >*Watch me, Mum; I **can** stand on one leg.*

  > ***All** we **can** see are his feet.*

### Capability (can/be able to)
- **Can**  
  Meaning 'know how to'. 

  With **adverbs of degree:**
  - *Almost*
  - *Hardly*
  - *Just*
  - *Nearly*
  
  > *I **can nearly** touch the ceiling.*
  
  > *I **can** cook.*  

- **Be able to**  
  When confirming that you have the **time, physical means, or technical capacity to do something** in specific situations 
  
  >*I finished my homework early, so I **am able to** cook dinner tonight.*

### Senses or feelings (can)
- **Can**    
  **Sense verbs:** 
  - *Feel, Hear, Smell, Taste*

  **Stative verbs:** 
  - *Believe, Decide, Remember, Understand*
  
  > *I **could** remember the crash, but nothing after that.*

### Passive voice (can)
- **Can**  

  >*Films **can** now easily **be streamed** online.*

## Past abilities
### Single past achievement (be able to)
- **Be able to**
  
  > *She swam strongly and **was able to** cross the river easily even though it was swollen by the heavy rain.*  

### General past abilities (could)
- **Could**

  > *When I was a teenage, I **could** hold my breath for two minutes*

  > *During the war, the police **could** arrest you for criticising the government.*

### Negative past achievements (couldn't/wasn't able to)
- **Wasn't able to**   
  Used in formal writing

  > *The test was extremely hard, and I **wasn't able to** pass it.*

- **Couldn't**  
  Use in informal daily speeches

  > *I **couldn't** finish the exam*

## Permission
### General actions (can/be allowed to)
- **Can/Be allowed to**  
  
  > *Anyone **could/was allowed** to fish in the lake when the council owned it.*

### Particular actions (be allowed to)
- **Be allowed to**
  
  > *Although he didn't have a ticket, Ned **was allowed to** come in.*

### Prohibitions (can't/be not allowed)
- **Can't/Be not allowed**

  > *You **can't/are not allowed to** enter!*

# (Modals) Degree of Certainty & Deductions
## Degrees of certainty 
### General truth (can)  
- **Can**  
  Usually stating **general facts**.  

  :warning: Substituting "Could" will give a different meaning
  
  >*It **can** be expensive to keep a cat.*
  
  > *We **can** stay with Jake in Oslo*

### Theoretical possibilities (could)
- **Could**  
  **If something happened**, it could, or it may not be.  

  >*It **could** be expensive to keep a cat.*

### Expectation (should/ought to)
- **Should**  
  More commonly used 
  
  >*You **should** be ready to read.*
  
- **Ought to**  
  Mainly used in formal writings/speeches.  

  >*You **ought to** be ready to begin.*

### Possible (may/might/could (have))
| Event Timeframe | Modal Construction | Context / Usage | Example(s) |
| :--- | :--- | :--- | :--- |
| **Present** | May | - In **academic or formal language** to talk about<br> characteristics or behaviours. | - *The seeds from the plant **may** grow up to 20 cm in length.* |
|| Might | - **Informal** speeches. | - *I **might** paint the kitchen purple.* |
| **Present<br> Continuous** | May/Might/Could + be + -ing | - An **ongoing** current event. | - *Marco isn't in his office. He **may/might/could be working**<br> at home today.* |
| **Past** | May/Might/Could + have + (past participle) | - Past **finished** events. | - *Do you think Laura **may/might have** completed the report<br> by now?* |
| **Past<br> Continuous** | May/Might/Could + have been + -ing | - Past **over a period of time.** | - *Callum didn't know where the wall was, but he thought<br> his sister **might/may/could have been playing**<br> with it before she left for school.* |
| **Past<br> Typical** | Might + (bare infinitive) | - Used to talk about what was **typically**<br> the case in the **past** in **formal** or **literary** use. | - *During the war, the police **might** arrest you for<br> criticising the government.* |
| **Future** | Present/Past expressions | - Use the expression for **present and past event**<br> with a **future deadline**. | - *His math **may/might/could have improved by the time**<br> the exam comes round.*<br> - ***When** I go to Vienna **I may/might/could be staying** with Max,<br> but I'm not sure yet.* |

### Impossible (can't/couldn't)
- **Can't**   
  Imply a **strong, confident deduction** about reality. It means you are looking at the **facts right** now and concluding that something is impossible
  
  > *There **can't** be many people in the world who haven't watched television.*

- **Couldn't**  
  It makes the statement feel slightly more **theoretical, remote, or imagined**.  

  > *That **couldn't** be the fastest route to Moscow; it adds ten hours to the travel time.*

## Logical deductions 
### Strong deductions (must have)
- **Must + have + (past participle)**  
  A strong deduction based on evidences. 

  >*That's not Clara's car. She **must have borrowed** it from her parents*

### Present events (must be/have (got) to be)
- **Must be + (-ing)**  
  Something happening at or around the time of speaking.  

  > *I can't hear a noise. You **must be imagining** things.*  

- **Must be + (bare infinitive)/Have (got) to be**  
  Informal present situation

  > *Their goalkeeper **has got to be/must be** at least two metres tall!*  

### Future (must be going)
- **Must be going**
  
  > *-What are the workmen doing?*  
  > *-I think they **must be going** to dig up the road.*  

# (Modals) Habits & Truth 
## General truths and habits
### General behaviour or habits (will)
- **Will**  
  Would for past.  
  :warning: **NOT for particular occasions**

  > ***Every day** Dan **will** come home from work and turn on the TV.*

  > ***Each time** I gave him a problem he **would** solve it for me.*

### Facts (will)
- **Will**
  Things that are **always true**
  
  >*Cold weather **will** kill certain plants*

  >*During the war, people **would** eat all kinds of things that we don't eat now.*

### Non-essential criteria (needn't/don't have to)
- **Needn't/Don't have to**
  > *Volcanoes **needn't/don't have to** erupt constantly to be classified as active.*

### Criticism in speech (will)
- We can **stress will or would** to **criticise** people's characteristic behaviour or habits.  

- Use **will** to express disapproval.

  >*-I feel sick*  
  >*-If you **will** eat so much, I'm not surprised*

## Past events/situations
### Clear time reference (would/used to)
- **Would/Used to**  

  >*Whenever we went to my uncle's house, we **would/used to** play in the garden.*

### Without clear time reference (used to)
- **Used to**
  To describe a **past state**. 

  >*We **used to** play in the garden.*
  
  >*The factory **used to** be over there.*
 
### The imagined past (would have)
- **Would have + (past participle)**  
  Imaginary situation or situation that **might have happened** in the past

  > *I **would have been happy** to see him, but I didn't have time*

### The assumed past (will have)
- **Will have + (past participle)**  
  Think a past situation **actually happened**.   

  >*As it was cloudy, few people **will have seen** last night's lunar eclipse*

# (Modals) Obligation, Advice & Reaction 
## Formal rules and warnings (must/must not) 
- **Must/Must not**

  >*Bookings **must** be made at least seven days before departure*

## Obligation 
### Inferred obligations (must have to)
- **Must have to**  
  Based on **current evidence** to make a **logical assumption** that someone else is forced or required to do something.  
  
  >*I can't access the database. You **must have to** put in a password.*

### External obligations (have (got) to)
- **Have to (formal)**  
  When used with **frequency words.**
  - *Always*
  - *Never*
  - *Normally* 
  - *Rarely*
  - *Sometimes*

  >*I **often have to** work at the weekend to get everything done.*

  With other **modal verbs.** 

  >*Motorists **will have to** wait until next year to use the bridge*  

- **Have got to (informal)**   
  If have is **contracted** (I've, He's, It'd)

  >*I need a new pair of shoes, and **they've got to** be blue.* 

### Lack of obligation (not have to)
- **Not have to**  
  When **somebody else** or **external rules** make something unnecessary

  > *We've been told that we **don't have to** be at work until ten tomorrow*

## Necessity 
### Practical or internal necessity (need/need to)
- **Need to/need**  
  Used in **informal language**

  > *I **needed to** leave early*

  > *She's thirsty. She **needs** a drink*

### General necessity (need to)
- >*You **need to** be over 18 to get into a nightclub.*  

### Lack of necessity (needn't/not need to) 
- **Needn't**  
  Often used in **formal language**. When it is the **speaker** who decides the lack of necessity 

  Often used with:
  - *Apply*
  - *Concern*
  - *Fear*
  - *Involve*
  - *Mean*
  - *Panic*

  > *I was very nervous before the interview, but I **needn't** have worried - I got the job!*

  >*You **needn't cut** the grass, I'll do it later.* 

- **Not need to** 
  Often used in informal daily speeches.  

  >*I **don't need** to wake up early tomorrow*

## Recommendations
### General comments (should/ought to)
- **Should**  
  Commonly be used. 

  >*You **should** finish your homework before going out.*

  Giving advice **with "I"**

  > ***I should** leave early tomorrow*

  **Outside authority** recommends 

  >*The manual says that the computer **should** be disconnected from the power supply before the cover is removed.*

- **Ought to**  
  Formal writings or speeches

  >*You **ought to** finish your homework before you go out.*

### Present, specific comments (had better)
- **Had better (informal)**  
  To express particular **urgency or in demands and threats**

  >*If you're not well, **you'd better** ask Clare to go instead.*

## Reaction to past events
### Expressing regret (should/ought to have)
- **Should/Ought to have + (past participle)**

  >*We **should/ought to have** waited for the rain to stop.*

### Expressing criticism (shouldn't/oughtn't to have)
- **Shouldn't/Oughtn't to have + (past participle)**

  >*We **shouldn't/oughtn't to have** gone to that place.*

# Advanced Syntactic Patterns  
## Compensation 
- **May/might not + (bare infinitive) ... but ...**  
  May/might not have + (past participle) ... but ... (past tense).  

  We say that a person or thing **compensates** to some extent for a **limitation** or **weakness** by having **another characteristic.**

  >*The painting **may not be** a masterpiece, **but** the colours are remarkable.*


</div>