

# Parallel Programming Models {.section}


## Distributed memory / Message Passing Model

::: {style="text-align: center;"}
<img src="img/parallel1.png" width=600>
:::

## Data parallel model

::: {style="text-align: center;"}
<img src="img/parallel2.png" width=600>
:::

## Hybrid model

::: {style="text-align: center;"}
<img src="img/parallel4.png" width=500>
:::
::: {style="text-align: center;"}
<img src="img/parallel3.png" width=500>
:::


## Partitioning data

::: {style="text-align: center;"}
<img src="img/parallel5.png" width=600>
:::



## Designing parallel programs

+ Data partitioning
+ Communication
+ Synchronization / Orchestration
+ Data dependencies
+ Load balancing
+ Input and Output (I/O)
+ Debugging

::: {.fragment}

A lot of these components are data engineering and DevOps issues
:::
::: {.fragment}

Infrastructures have standardized many of these and have helped data scientists implement parallel programming much more easily
:::
::: {.fragment}

We'll see in the lab how the `multiprocessing` module in Python makes parallel processing on a machine quite easy to implement
:::
