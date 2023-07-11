<script lang="ts">
  // import axios from 'axios';
  import { onMount, createEventDispatcher } from 'svelte';

  let daysOfWeek = [
    { name: 'Monday', selected: false },
    { name: 'Tuesday', selected: false },
    { name: 'Wednesday', selected: false },
    { name: 'Thursday', selected: false },
    { name: 'Friday', selected: false },
    { name: 'Saturday', selected: false },
    { name: 'Sunday', selected: false }
  ];

  let selectAll = false;

  const toggleAll = () => {
    selectAll = !selectAll;
    daysOfWeek = daysOfWeek.map((day) => ({ ...day, selected: selectAll }));
  };

  let goalDate: string;
  let goalTime: string;

  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch('save');
    // add your saving logic here
  }

  let loadingGenerate = false;
  let loadingRegenerate = false;

  const handleClickGenerate = async () => {
    loadingGenerate = true;
    // Simulate an API call delay
    await new Promise((resolve) => setTimeout(resolve, 2000));
    loadingGenerate = false;
  };

  const handleClickRegenerate = async () => {
    loadingRegenerate = true;
    // Simulate an API call delay
    await new Promise((resolve) => setTimeout(resolve, 2000));
    loadingRegenerate = false;
  };

  onMount(async () => {
    // Fetch data from API
    // const response = await axios.get('your-api-endpoint');
    // const data = response.data;
    // Assign the fetched data to variables or update the necessary parts of the component
    // goalDate = data.goalDate;
    // goalTime = data.goalTime;
  });

  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  function regenerate(event: MouseEvent & { currentTarget: EventTarget & HTMLButtonElement }) {
    throw new Error('Function not implemented.');
  }
</script>

<div class="hero min-h-screen bg-base-200 mb-10">
  <div class="flex flex-col lg:flex-row justify-around items-center lg:items-start hero-content">
    <div class="text-center lg:text-left lg:w-1/2">
      <h1 class="text-5xl font-bold">Smart Tracking Your Goals.</h1>
      <p class="py-6">
        SMART Goal AI is a sophisticated tool leveraging artificial intelligence to assist users in
        formulating, tracking, and accomplishing their goals using the SMART (Specific, Measurable,
        Achievable, Relevant, Time-bound) methodology. It refines users' goals for clarity and
        realism and integrates features for tracking progress, including customizable reminders. The
        app promotes consistent habits by enabling users to schedule daily reminders, creating an
        effective and efficient platform for personal and professional growth.
      </p>
    </div>
    <div class="card flex-shrink-0 w-full lg:w-1/3 max-w-sm shadow-2xl bg-base-100">
      <div class="card-body">
        <div class="form-control">
          <label class="label" for="email-input">
            <span class="label-text">Email</span>
          </label>
          <input type="text" placeholder="email" id="email-input" class="input input-bordered" />
        </div>

        <div class="form-control">
          <label class="label" for="password-input">
            <span class="label-text">Password</span>
          </label>
          <input
            type="password"
            placeholder="password"
            id="password-input"
            class="input input-bordered"
          />
          <a href={'#'} class="label-text-alt link link-hover mt-4 mb-4">Forgot password?</a>
          <a href={'#'} class="label-text-alt link link-hover"
            >Are your Goals Smart yet? Sign up here!</a
          >
        </div>
        <div class="form-control mt-6">
          <button class="btn btn-primary">Login</button>
        </div>
        <div class="form-control mt-6 text-center text-lg font-bold" />
      </div>
    </div>
  </div>
</div>

<div class="flex">
  <div class="divider" />
</div>
<div class="container mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10">
  <div class="mb-5">
    <label class="block text-xl font-bold mb-2" for="goal"> Goal </label>
    <input
      class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
      id="goal"
      type="text"
      placeholder="What's your SMART Goal?"
    />

    <div class="mt-3 flex flex-col items-left">
      <button
        id="generate"
        class="btn btn-primary"
        on:click={handleClickGenerate}
        disabled={loadingGenerate}
      >
        Generate
      </button>
      {#if loadingGenerate}
        <div class="mt-3 flex justify-center items-center">
          <span class="loading loading-infinity loading-md" />
        </div>
      {/if}
    </div>
    <div class="mt-3 flex flex-col items-right">
      <button
        id="regenerate"
        class="btn btn-primary"
        on:click={handleClickRegenerate}
        disabled={loadingRegenerate}
      >
        Regenerate
      </button>
      {#if loadingRegenerate}
        <div class="mt-3 flex justify-center items-center">
          <span class="loading loading-infinity loading-md" />
        </div>
      {/if}
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
    <!-- Specific card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Specific</h2>
          <p id="specific" class="text-gray-600" contenteditable="true">
            SmartGoalAI's Specific suggestion
          </p>
          <div class="mt-3">
            <button on:click={regenerate} class="btn btn-primary">Regenerate</button>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Measurable card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Measurable</h2>
          <p id="measurable" class="text-gray-600" contenteditable="true">
            SmartGoalAI's Measurable suggestion
          </p>
          <div class="mt-3">
            <button on:click={regenerate} class="btn btn-primary">Regenerate</button>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Attainable card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Attainable</h2>
          <p id="attainable" class="text-gray-600" contenteditable="true">
            SmartGoalAI's Attainable suggestion
          </p>
          <div class="mt-3">
            <button on:click={regenerate} class="btn btn-primary">Regenerate</button>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Relevant card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Relevant</h2>
          <p id="relevant" class="text-gray-600" contenteditable="true">
            SmartGoalAI's Relevant suggestion
          </p>
          <div class="mt-3">
            <button on:click={regenerate} class="btn btn-primary">Regenerate</button>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Time-Bound card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Time-Bound</h2>
          <p id="time-bound" class="text-gray-600" contenteditable="true">
            SmartGoalAI's Time-Bound suggestion
          </p>
          <div class="mt-3">
            <button on:click={regenerate} class="btn btn-primary">Regenerate</button>
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
</div>

<div class="mt-4 pd-4 flex flex-col items-center">
  <span class="block text-xl font-bold mb-2">Days of the week</span>
  <button class="btn btn-primary mt-4" on:click={toggleAll}>
    {#if selectAll}Deselect All{:else}Select All{/if}
  </button>
  <div class="grid grid-cols-2 md:grid-cols- gap-5 mt-4">
    {#each daysOfWeek as day (day.name)}
      <div class="rounded shadow p-2">
        <label class="inline-flex items-center">
          <input
            type="checkbox"
            class={day.selected ? 'toggle toggle-primary' : 'toggle toggle-info'}
            bind:checked={day.selected}
          />
          <span class="ml-2 text-md">{day.name}</span>
        </label>
      </div>
    {/each}
  </div>
</div>

<div class="mt-4 flex flex-col items-center">
  <label class="block text-lg font-bold mb-2" for="goal-date"> Date </label>
  <input
    bind:value={goalDate}
    class="shadow appearance-none border rounded w-1/2 py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
    id="goal-date"
    type="date"
  />
  <label class="block text-lg font-bold mb-2 mt-4" for="goal-time"> Time </label>
  <input
    bind:value={goalTime}
    class="shadow appearance-none border rounded w-1/2 py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
    id="goal-time"
    type="time"
  />
</div>

<div class="mt-4 flex flex-col items-center">
  <button class="btn btn-primary" on:click={handleClick}>Save Smart Goal</button>
</div>
