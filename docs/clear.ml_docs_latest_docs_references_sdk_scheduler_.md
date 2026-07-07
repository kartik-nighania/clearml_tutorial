---
url: "https://clear.ml/docs/latest/docs/references/sdk/scheduler/"
title: "TaskScheduler | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/scheduler/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ automation.TaskScheduler(sync\_frequency\_minutes=15, force\_create\_task\_name=None, force\_create\_task\_project=None) [​](https://clear.ml/docs/latest/docs/references/sdk/scheduler/\#class-automationtaskschedulersync_frequency_minutes15-force_create_task_namenone-force_create_task_projectnone "Direct link to class-automationtaskschedulersync_frequency_minutes15-force_create_task_namenone-force_create_task_projectnone")

Task Scheduling controller.
Notice time-zone is ALWAYS UTC

Create a Task scheduler service

- **Parameters**
  - **sync\_frequency\_minutes** (`float`) – Sync task scheduler configuration every X minutes.
    Allow to change scheduler in runtime by editing the Task configuration object

  - **force\_create\_task\_name** (`Optional`\[`str`\]) – Optional, force creation of Task Scheduler service,
    even if main Task.init already exists.

  - **force\_create\_task\_project** (`Optional`\[`str`\]) – Optional, force creation of Task Scheduler service,
    even if main Task.init already exists.

* * *

### add\_task [​](https://clear.ml/docs/latest/docs/references/sdk/scheduler/\#add_task "Direct link to add_task")

**add\_task(schedule\_task\_id=None, schedule\_function=None, queue=None, name=None, target\_project=None, minute=None, hour=None, day=None, weekdays=None, month=None, year=None, limit\_execution\_time=None, single\_instance=False, recurring=True, execute\_immediately=False, reuse\_task=False, task\_parameters=None, task\_overrides=None)**

Create a cron job-like scheduling for a pre-existing Task.
Notice, it is recommended to give the schedule entry a descriptive unique name,
if not provided, a name is randomly generated.

When timespec parameters are specified exclusively, they define the time between task launches (see
year and weekdays exceptions). When multiple timespec parameters are specified, the parameter representing
the longest duration defines the time between task launches, and the shorter timespec parameters define specific
times.

Examples:

Launch every 15 minutes:

```py
add_task(schedule_task_id='1235', queue='default', minute=15)
```

Launch every 1 hour:

```py
add_task(schedule_task_id='1235', queue='default', hour=1)
```

Launch every 1 hour at hour:30 minutes (i.e. 1:30, 2:30 etc.):

```py
add_task(schedule_task_id='1235', queue='default', hour=1, minute=30)
```

Launch every day at 22:30 (10:30 pm):

```py
add_task(schedule_task_id='1235', queue='default', minute=30, hour=22, day=1)
```

Launch every other day at 7:30 (7:30 am):

```py
add_task(schedule_task_id='1235', queue='default', minute=30, hour=7, day=2)
```

Launch every Saturday at 8:30am (notice day=0):

```py
add_task(schedule_task_id='1235', queue='default', minute=30, hour=8, day=0, weekdays=['saturday'])
```

Launch every 2 hours on the weekends Saturday/Sunday (notice day is not passed):

```py
add_task(schedule_task_id='1235', queue='default', hour=2, weekdays=['saturday', 'sunday'])
```

Launch once a month at the 5th of each month:

```py
add_task(schedule_task_id='1235', queue='default', month=1, day=5)
```

Launch once a year on March 4th:

```py
add_task(schedule_task_id='1235', queue='default', year=1, month=3, day=4)
```

- **Parameters**
  - **schedule\_task\_id** (`Union`\[`str`, [`Task`](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task), `None`\]) – ID of Task to be cloned and scheduled for execution

  - **schedule\_function** (`Optional`\[`Callable`\]) – Optional, instead of providing Task ID to be scheduled,
    provide a function to be called. Notice the function is called from the scheduler context
    (i.e. running on the same machine as the scheduler)

  - **queue** (`Optional`\[`str`\]) – Name or ID of queue to put the Task into (i.e. schedule)

  - **name** (`Optional`\[`str`\]) – Name or description for the cron Task (should be unique if provided, otherwise randomly generated)

  - **target\_project** (`Optional`\[`str`\]) – Specify target project to put the cloned scheduled Task in.

  - **minute** (`Optional`\[`int`\]) – Time (in minutes) between task launches. If specified together with hour, day, month,
    and / or year, it defines the minute of the hour

  - **hour** (`Optional`\[`int`\]) – Time (in hours) between task launches. If specified together with day, month, and / or
    year, it defines the hour of day.

  - **day** (`Optional`\[`int`\]) – Time (in days) between task executions. If specified together with month and / or year,
    it defines the day of month

  - **weekdays** (`Optional`\[`List`\[`str`\]\]) – Days of week to launch task (accepted inputs: ‘monday’, ‘tuesday’, ‘wednesday’,
    ‘thursday’, ‘friday’, ‘saturday’, ‘sunday’)

  - **month** (`Optional`\[`int`\]) – Time (in months) between task launches. If specified with year, it defines a specific month

  - **year** (`Optional`\[`int`\]) – Specific year if value >= current year. Time (in years) between task launches if
    value <= 100

  - **limit\_execution\_time** (`Optional`\[`float`\]) – Limit the execution time (in hours) of the specific job.

  - **single\_instance** (`bool`) – If True, do not launch the Task job if the previous instance is still running
    (skip until the next scheduled time period). Default False.

  - **recurring** (`bool`) – If False, only launch the Task once (default: True, repeat)

  - **execute\_immediately** (`bool`) – If True, schedule the Task to be executed immediately
    then recurring based on the timing schedule arguments. Default False.

  - **reuse\_task** (`bool`) – If True, re-enqueue the same Task (i.e. do not clone it) every time, default False.

  - **task\_parameters** (`Optional`\[`dict`\]) – Configuration parameters to the executed Task.
    for example: `{'Args/batch': '12'}` Notice: not available when reuse\_task=True

  - **task\_overrides** (`Optional`\[`dict`\]) – Change task definition.
    for example `{'script.version_num': None, 'script.branch': 'main'}` Notice: not available when reuse\_task=True
- **Return type**

`bool`

- **Returns**

True if job is successfully added to the scheduling list


* * *

### get\_scheduled\_tasks [​](https://clear.ml/docs/latest/docs/references/sdk/scheduler/\#get_scheduled_tasks "Direct link to get_scheduled_tasks")

**get\_scheduled\_tasks()**

Return the current set of scheduled jobs

- **Return type**

`List`\[`ScheduleJob`\]

- **Returns**

List of ScheduleJob instances


* * *

### remove\_task [​](https://clear.ml/docs/latest/docs/references/sdk/scheduler/\#remove_task "Direct link to remove_task")

**remove\_task(task\_id)**

Remove a Task ID from the scheduled task list.

- **Parameters**

**task\_id** (`Union`\[`str`, [`Task`](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task), `Callable`\]) – Task or Task ID to be removed

- **Return type**

`bool`

- **Returns**

return True of the Task ID was found in the scheduled jobs list and was removed.


* * *

### start [​](https://clear.ml/docs/latest/docs/references/sdk/scheduler/\#start "Direct link to start")

**start()**

Start the Task TaskScheduler loop (notice this function does not return)

- **Return type**

`None`


* * *

### start\_remotely [​](https://clear.ml/docs/latest/docs/references/sdk/scheduler/\#start_remotely "Direct link to start_remotely")

**start\_remotely(queue='services')**

Start the Task TaskScheduler loop (notice this function does not return)

- **Parameters**

**queue** (`str`) – Remote queue to run the scheduler on, default ‘services’ queue.

- **Return type**

`None`


- [_class_ automation.TaskScheduler(sync\_frequency\_minutes=15, force\_create\_task\_name=None, force\_create\_task\_project=None)](https://clear.ml/docs/latest/docs/references/sdk/scheduler/#class-automationtaskschedulersync_frequency_minutes15-force_create_task_namenone-force_create_task_projectnone)
  - [add\_task](https://clear.ml/docs/latest/docs/references/sdk/scheduler/#add_task)
  - [get\_scheduled\_tasks](https://clear.ml/docs/latest/docs/references/sdk/scheduler/#get_scheduled_tasks)
  - [remove\_task](https://clear.ml/docs/latest/docs/references/sdk/scheduler/#remove_task)
  - [start](https://clear.ml/docs/latest/docs/references/sdk/scheduler/#start)
  - [start\_remotely](https://clear.ml/docs/latest/docs/references/sdk/scheduler/#start_remotely)