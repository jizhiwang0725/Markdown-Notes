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


- <a href="communication.md">Communication</a>
- <a href="complements.md">Complements</a>
- <a href="complex_structures.md">Complex Structures</a>
- <a href="future_actions.md">Future Actions</a>
- <a href="modals.md">Modals</a>
- <a href="passive_voice.md">Passive Voice</a>
- <a href="prepositional_phrase.md">Prepositional Phrase</a>
- <a href="tenses.md">Tenses</a>

<strong>Table of Contents</strong>

- [Verb Phrase (VP)](#verb-phrase-vp)
  - [Structural formula](#structural-formula)
- [Transitive Verb Patterns](#transitive-verb-patterns)
  - [Monotransitive](#monotransitive)
    - [V + DO](#v--do)
  - [Transitive prepositional](#transitive-prepositional)
    - [V + DO + prepositional phrase](#v--do--prepositional-phrase)
  - [Ditransitive](#ditransitive)
    - [V + IO + DO](#v--io--do)
    - [V + DO + prep + IO](#v--do--prep--io)
  - [Complex transitive](#complex-transitive)
    - [V + DO + object complement](#v--do--object-complement)
- [Intransitive Verb Patterns](#intransitive-verb-patterns)
  - [Unergative](#unergative)
  - [Unaccusative](#unaccusative)
  - [Linking](#linking)
    - [V + subject complement](#v--subject-complement)
  - [Intransitive prepositional](#intransitive-prepositional)
    - [V + preposition phrase](#v--preposition-phrase)
- [Ambitransitive Verb Patterns](#ambitransitive-verb-patterns)
  - [Transitive/Intransitive](#transitiveintransitive)



</div>

<div class='main-content'>

# Verb Phrase (VP)
## Structural formula 
- **[Auxiliaries] + HEAD VERB + [Complements/Objects] + [Adverbial Modifiers]**

- **Auxiliaries**  
  **Primary** auxiliaries that dictate **tense** or mood and **modal** auxiliaries

- **Adverbial Modifiers**  
  Explaining **when, where, or how** the action happened.
  - Adverb phrases  
  - Prepositional Phrases  
  
# Transitive Verb Patterns
## Monotransitive
### V + DO
- Follow by a **direct object**
  An action that happens **to** something or someone.   
  It requires a **direct object**, otherwise the sentence **feels incomplete**.  
  - *Drink, Chase, Hunt*

  > *She **closed** the **door.***
  
  Direct object is **NOT required** when it is clear from the **context**
  - *Sing, Answer, Ask, Cook, Dance, Read, Smoke, Study, Wash, Wash up, Wave, Win*

  > *She **plays** (the saxophone) beautifully.*

## Transitive prepositional  
### V + DO + prepositional phrase
- Some verbs requires a **preposition** and its corresponding **prepositional object**.  
  The prepositional phrase is used to describe 

  **<a href="prepositional_phrase.md">See in note about prepositional phrases</a>**

## Ditransitive
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

## Complex transitive 
### V + DO + object complement
- Some verbs requires an **object complement** to make the sentence complete 

  **<a href="complements.md#object-complements">See in note about object complements</a>**



# Intransitive Verb Patterns
## Unergative 
- The subject is the **agent**. 
  The subject is actively willfully and consciously **performing the action** 
  - *Run, Swim, Sing, Jump, Work, Talk, Laugh, Sneeze*

  > *The developer **laughed***

## Unaccusative
- The action is **happening to the subject**, or the subject is experiencing a change of state, condition or location 
  - *Fall, Die, Melt, Arrive, Disappear, Emerge, OCcur, Collapse*
  
  > *THe ice **melted***

## Linking
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

## Intransitive prepositional  
### V + preposition phrase
- Some verbs are **followed straight by a preposition**.  

  **<a href="prepositions.md">See in note about prepositions</a>**

# Ambitransitive Verb Patterns 
## Transitive/Intransitive
- **Words that can be either transitive or intransitive.**  
  Words that relate to a **change**   
  - *Bring, Bend, Break, Increase, Move, Open, Shut, Start, Vary, Weaken*
  
  > *She **closed** the door. (transitive)*  

  > *The door **closed**. (intransitive)*  

</div>