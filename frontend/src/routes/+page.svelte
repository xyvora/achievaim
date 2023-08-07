<script lang="ts">

  import { goto } from '$app/navigation';
  import ErrorMessage from '$lib/components/ErrorMessage.svelte';
  import Input from '$lib/components/Input.svelte';
  import { LoginError } from '$lib/errors';
  import { accessToken, isLoading, isLoggedIn } from '$lib/stores/stores';
  import type { Goals, UserLogin } from '$lib/types';
  import { login } from '$lib/api';
  import DaysOfWeekSelector from '$lib/components/DaysOfWeekSelector.svelte';
  import type { DaysOfWeekOutput } from '$lib/generated';
  import { toTitleCase } from '$lib/utils';

  // NOTE: Temporary, will be replaced will call to the API
  const daysOfWeek: DaysOfWeekOutput = {
    monday: true,
    tuesday: false,
    wednesday: true,
    thursday: false,
    friday: true,
    saturday: false,
    sunday: false
  };

  type DaysOfWeek = {
    monday: boolean;
    tuesday: boolean;
    wednesday: boolean;
    thursday: boolean;
    friday: boolean;
    saturday: boolean;
    sunday: boolean;
  };

  type Goal = {
    days_of_week: DaysOfWeek;
    date_for_achievement?: string;
    time_of_day?: string;
  };

  let goal: Goal = {
    days_of_week: {
      monday: false,
      tuesday: false,
      wednesday: false,
      thursday: false,
      friday: false,
      saturday: false,
      sunday: false
    }
  };


  import { page } from '$app/stores';

  let goals: Goals = {
    active: [
      {
        name: 'Active Placeholder',
        details: 'S.M.A.R.T details here',
        date: new Date('2024-01-01T10:00:00'),
        days: [10],
        editing: false
      }
    ],
    completed: [
      {
        name: 'Completed Placeholder',
        details: 'S.M.A.R.T details here',
        date: new Date('2024-01-02T14:00:00'),
        days: [15],
        editing: false
      }
    ]
  };

  let userLogin: UserLogin = {
    userName: '',
    password: ''
  };

  let userNameError = false;
  let passwordError = false;
  let genericError = false;
  let genericErrorMessage = '';

  async function handleSubmit() {
    isLoading.set(true);
    genericError = false;
    userNameError = false;
    passwordError = false;

    if (userLogin.userName == null || userLogin.userName.trim() === '') {
      userNameError = true;
    }

    if (userLogin.password == null || userLogin.password.trim() === '') {
      passwordError = true;
    }

    if (userNameError === true || passwordError === true) {
      isLoading.set(false);
      return;
    }

    try {
      const token = await login(userLogin);
      accessToken.set(token);
    } catch (error) {
      if (
        error instanceof LoginError &&
        error.message !== undefined &&
        error.message === 'Incorrect user name or password'
      ) {
        genericError = true;
        genericErrorMessage = 'Incorrect user name or password';
      } else {
        genericError = true;
        genericErrorMessage =
          'An error occurred trying to connect to the sever. Please try again later.';
      }
      isLoading.set(false);
      return;
    }
    userLogin.userName = '';
    userLogin.password = '';
    isLoading.set(false);
  }
</script>
<div class="page-fade-in">
{#if !$isLoggedIn}
  <div class="hero min-h-screen bg-base-200 mb-10">
    <div class="flex flex-col lg:flex-row justify-around items-center lg:items-start hero-content">
      <div class="text-center lg:text-left lg:w-1/2">
        <h1 class="text-5xl font-bold">Smart Tracking Your Goals.</h1>
        <p class="py-6">
          Achiev𝘼𝙄m (pronounced "AchieveAim" or "uh-cheev-aim", IPA: /əˈtʃi:v eɪm/) is a
          sophisticated tool leveraging artificial intelligence to assist users in formulating,
          tracking, and accomplishing their goals using the SMART (Specific, Measurable, Achievable,
          Relevant, Time-bound) methodology. It refines users' goals for clarity and realism and
          integrates features for tracking progress, including customizable reminders. The app
          promotes consistent habits by enabling users to schedule daily reminders, creating an
          effective and efficient platform for personal and professional growth.
        </p>
      </div>
      <div class="card flex-shrink-0 w-full lg:w-1/3 max-w-sm shadow-2xl bg-base-100">
        <div class="card-body">
          <form
            on:submit|preventDefault={handleSubmit}
            class="w-full max-w-lg mx-auto my-10 p-5 rounded shadow"
          >
            <Input
              inputId="user-name"
              labelText="User Name"
              placeholder="user name"
              errorMessage="User Name is required."
              isError={userNameError}
              bind:value={userLogin.userName}
            />

            <Input
              inputId="password"
              labelText="Password"
              placeholder="password"
              errorMessage="Password is required."
              isError={passwordError}
              bind:value={userLogin.password}
              isPassword={true}
            />

            <ErrorMessage
              errorMessageId="generic-error"
              errorMessage={genericErrorMessage}
              showError={genericError}
            />

            <div class="form-control">
              <a href={'#'} class="label-text-alt link link-hover mt-4 mb-4">Forgot password?</a>
              <a
                href="signup"
                class="label-text-alt link link-hover"
                class:active={$page.url.pathname === '/signup'}
                >Are your Goals Smart yet? Sign up here!</a
              >
            </div>
            {#if $isLoading}
              <div class="mt-6 text-center">
                <span class="loading loading-spinner text-primary" id="login-spinner" />
              </div>
            {:else}
              <div class="form-control mt-6">
                <button class="btn btn-primary" type="submit" id="login-button">Login</button>
              </div>
            {/if}
            <div class="form-control mt-6 text-center text-lg font-bold" />
          </form>
        </div>
      </div>
    </div>
  </div>
{:else}
<div class="container mx-auto px-4 py-8">
  <!-- The 'container' class sets a max-width and centers the content horizontally -->

  <div class="md:flex md:space-x-4">
    <!-- Left Column (Cards will appear above each other on smaller screens) -->
    <div class="md:w-1/2 md:mb-0 mb-4 md:pr-2">
      <h2 class="text-xl font-bold mb-2">Active</h2>

      <!-- Card 1 -->
      <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
      <div
        tabindex="0"
        class="collapse md:ml-3 mb-3 bg-primary text-primary-content focus:bg-secondary focus:text-secondary-content"
      >
        <div class="collapse-title">
          <div
            class="container shadow-lg rounded-xl mb-4 mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10"
          >
            <div class="mb-5">
              <div class="card w-full">
                <figure>
                  <figcaption class="p-4 card-body flex flex-col">
                    <div class="flex items-center mb-2">
                      <a
                        href="/edit-goal"
                        aria-label="edit-goal"
                        title="Edit Goal"
                        class="{$page.url.pathname === '/edit-goal'
                          ? 'rounded bg-white'
                          : ''} block text-xl font-bold mr-2"
                      >
                        Goal
                      </a>
                      <div class="dropdown dropdown-right">
                        <button class="btn btn-circle btn-ghost btn-xs text-info">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            class="w-4 h-4 stroke-white"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                            />
                          </svg>
                        </button>
                        <button
                          class="card compact text-left text-primary dropdown-content z-[1] shadow bg-base-100 rounded-box w-64"
                        >
                          <div class="card-body">
                            <p>Click the Goal Text to the left to edit your SMART goal.</p>
                          </div>
                        </button>
                      </div>
                    </div>
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                    >
                      What's your SMART Goal?
                    </div>
                  </figcaption>
                </figure>
              </div>
            </div>
          </div>
        </div>
        <div class="collapse-content">
          <div
            class="container shadow-lg rounded-xl mb-4 mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10"
          >
            <!-- Rest of the Content goes here -->
            <!-- Specific card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Specific</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Specific suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <!-- Measurable card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Measurable</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Measurable suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <!-- Attainable card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Attainable</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Attainable suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <!-- Relevant card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Relevant</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Relevant suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <!-- Time-Bound card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Time-Bound</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Time-Bound suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <div class="mt-3 flex flex-col items-center">
              <div class="card w-full">
                <figure>
                  <figcaption class="p-4 card-body flex flex-col items-center">
                    {#if goal.days_of_week}
                      <div class="flex justify-between items-center w-full">
                        <h2 class="card-title mb-2">Days</h2>
                      </div>
                      <DaysOfWeekSelector daysOfWeek={goal.days_of_week} />
                    {/if}
                  </figcaption>
                </figure>
              </div>
            </div>

            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-row items-center">
                  <h2 class="card-title mb-2">Date</h2>
                  <div class="flex-grow flex items-center relative">
                    <input
                      class="shadow text-secondary appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                      id="goal-date"
                      type="date"
                      bind:value={goal.date_for_achievement}
                      aria-describedby="date-description"
                      readonly
                    />
                  </div>
                </figcaption>
              </figure>
            </div>

            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-row items-center">
                  <h2 class="card-title mb-2">Time</h2>
                  <div class="flex-grow flex items-center">
                    <input
                      class="shadow text-secondary appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                      id="goal-time"
                      type="time"
                      bind:value={goal.time_of_day}
                      aria-describedby="time-description"
                      readonly
                    />
                  </div>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
      <div
        tabindex="0"
        class="collapse md:ml-3 mb-3 bg-primary text-primary-content focus:bg-secondary focus:text-secondary-content"
      >
        <div class="collapse-title">
          <div
            class="container shadow-lg rounded-xl mb-4 mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10"
          >
            <div class="mb-5">
              <div class="card w-full">
                <figure>
                  <figcaption class="p-4 card-body flex flex-col">
                    <div class="flex items-center mb-2">
                      <a
                        href="/edit-goal"
                        aria-label="edit-goal"
                        title="Edit Goal"
                        class="{$page.url.pathname === '/edit-goal'
                          ? 'rounded bg-white'
                          : ''} block text-xl font-bold mr-2"
                      >
                        Goal
                      </a>
                      <div class="dropdown dropdown-right">
                        <button class="btn btn-circle btn-ghost btn-xs text-info">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            class="w-4 h-4 stroke-white"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                            />
                          </svg>
                        </button>
                        <button
                          class="card compact text-left text-primary dropdown-content z-[1] shadow bg-base-100 rounded-box w-64"
                        >
                          <div class="card-body">
                            <p>Click the Goal Text to the left to edit your SMART goal.</p>
                          </div>
                        </button>
                      </div>
                    </div>
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                    >
                      What's your SMART Goal?
                    </div>
                  </figcaption>
                </figure>
              </div>
            </div>
          </div>
        </div>
        <div class="collapse-content">
          <div
            class="container shadow-lg rounded-xl mb-4 mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10"
          >
            <!-- Rest of the Content goes here -->
            <!-- Specific card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Specific</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Specific suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <!-- Measurable card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Measurable</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Measurable suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <!-- Attainable card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Attainable</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Attainable suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <!-- Relevant card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Relevant</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Relevant suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <!-- Time-Bound card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Time-Bound</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Time-Bound suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <div class="mt-3 flex flex-col items-center">
              <div class="card w-full">
                <figure>
                  <figcaption class="p-4 card-body flex flex-col items-center">
                    {#if goal.days_of_week}
                      <div class="flex justify-between items-center w-full">
                        <h2 class="card-title mb-2">Days</h2>
                      </div>
                      <DaysOfWeekSelector daysOfWeek={goal.days_of_week} />
                    {/if}
                  </figcaption>
                </figure>
              </div>
            </div>

            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-row items-center">
                  <h2 class="card-title mb-2">Date</h2>
                  <div class="flex-grow flex items-center relative">
                    <input
                      class="shadow text-secondary appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                      id="goal-date"
                      type="date"
                      bind:value={goal.date_for_achievement}
                      aria-describedby="date-description"
                      readonly
                    />
                  </div>
                </figcaption>
              </figure>
            </div>

            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-row items-center">
                  <h2 class="card-title mb-2">Time</h2>
                  <div class="flex-grow flex items-center">
                    <input
                      class="shadow  appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                      id="goal-time"
                      type="time"
                      bind:value={goal.time_of_day}
                      aria-describedby="time-description"
                      readonly
                    />
                  </div>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Right Column -->
    <div class="md:w-1/2 md:ml-4 md:pl-2">
      <h2 class="text-xl font-bold mb-2">Completed</h2>

      <!-- Card 3 -->
      <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
      <div
        tabindex="0"
        class="collapse md:ml-3 mb-3 bg-primary text-primary-content focus:bg-secondary focus:text-secondary-content"
      >
        <div class="collapse-title">
          <div
            class="container shadow-lg rounded-xl mb-4 mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10"
          >
            <div class="mb-5">
              <div class="card w-full">
                <figure>
                  <figcaption class="p-4 card-body flex flex-col">
                    <div class="flex items-center mb-2">
                      <a
                        href="/edit-goal"
                        aria-label="edit-goal"
                        title="Edit Goal"
                        class="{$page.url.pathname === '/edit-goal'
                          ? 'rounded bg-white'
                          : ''} block text-xl font-bold mr-2"
                      >
                        Goal
                      </a>
                      <div class="dropdown dropdown-right">
                        <button class="btn btn-circle btn-ghost btn-xs text-info">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            class="w-4 h-4 stroke-white"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                            />
                          </svg>
                        </button>
                        <button
                          class="card compact text-left text-primary dropdown-content z-[1] shadow bg-base-100 rounded-box w-64"
                        >
                          <div class="card-body">
                            <p>Click the Goal Text to the left to edit your SMART goal.</p>
                          </div>
                        </button>
                      </div>
                    </div>
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                    >
                      What's your SMART Goal?
                    </div>
                  </figcaption>
                </figure>
              </div>
            </div>
          </div>
        </div>
        <div class="collapse-content">
          <div
            class="container shadow-lg rounded-xl mb-4 mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10"
          >
            <!-- Rest of the Content goes here -->
            <!-- Specific card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Specific</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Specific suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <!-- Measurable card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Measurable</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Measurable suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <!-- Attainable card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Attainable</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Attainable suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <!-- Relevant card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Relevant</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Relevant suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <!-- Time-Bound card -->
            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <h2 class="card-title mb-2">Time-Bound</h2>
                  <div class="flex flex-col md:flex-row w-full">
                    <div
                      class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
                    >
                      AchievAIm's Time-Bound suggestion
                    </div>
                  </div>
                </figcaption>
              </figure>
            </div>

            <div class="mt-3 flex flex-col items-center">
              <div class="card w-full">
                <figure>
                  <figcaption class="p-4 card-body flex flex-col items-center">
                    {#if goal.days_of_week}
                      <div class="flex justify-between items-center w-full">
                        <h2 class="card-title mb-2">Days</h2>
                      </div>
                      <DaysOfWeekSelector daysOfWeek={goal.days_of_week} />
                    {/if}
                  </figcaption>
                </figure>
              </div>
            </div>

            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-row items-center">
                  <h2 class="card-title mb-2">Date</h2>
                  <div class="flex-grow flex items-center relative">
                    <input
                      class="shadow text-secondary appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                      id="goal-date"
                      type="date"
                      bind:value={goal.date_for_achievement}
                      aria-describedby="date-description"
                      readonly
                    />
                  </div>
                </figcaption>
              </figure>
            </div>

            <div class="card w-full">
              <figure>
                <figcaption class="p-4 card-body flex flex-row items-center">
                  <h2 class="card-title mb-2">Time</h2>
                  <div class="flex-grow flex items-center">
                    <input
                      class="shadow text-secondary appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                      id="goal-time"
                      type="time"
                      bind:value={goal.time_of_day}
                      aria-describedby="time-description"
                      readonly
                    />
                  </div>
                </figcaption>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

{/if}

<style>
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  .page-fade-in {
    animation: fadeIn 1s ease-in-out;
  }
</style>
</div>