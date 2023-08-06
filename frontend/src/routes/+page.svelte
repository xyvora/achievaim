<script lang="ts">
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';
  import ErrorMessage from '$lib/components/ErrorMessage.svelte';
  import Input from '$lib/components/Input.svelte';
  import { LoginError } from '$lib/errors';
  import { accessToken, isLoading, isLoggedIn } from '$lib/stores/stores';
  import type { Goals, UserLogin } from '$lib/types';
  import { login } from '$lib/api';
  import DaysOfWeekSelector from '$lib/components/DaysOfWeekSelector.svelte';
  import type { DaysOfWeek } from '$lib/generated';
  import { toTitleCase } from '$lib/utils';

  // NOTE: Temporary, will be replaced will call to the API
  const daysOfWeek: DaysOfWeek = {
    monday: true,
    tuesday: false,
    wednesday: true,
    thursday: false,
    friday: true,
    saturday: false,
    sunday: false
  };

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
  <div class="container mx-auto p-4">
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
      {#each Object.entries(goals) as [category, value]}
        <div class="bg-white rounded shadow overflow-hidden">
          <div class="bg-gray-200 text-gray-700 text-lg sm:text-xl font-semibold p-3">
            {toTitleCase(category)}
          </div>
          <div class="p-4">
            {#if value.length === 0}
              <div
                class="bg-gray-100 border-2 border-dashed border-gray-200 rounded-lg h-40 flex items-center justify-center text-gray-500"
              >
                Add a Goal
              </div>
            {:else}
              {#each value as goal (goal.name)}
                <div
                  class={`rounded-lg p-4 sm:p-6 mb-4 ${
                    goal.placeholder ? 'bg-gray-200' : 'bg-white'
                  } shadow-sm border border-gray-200 space-y-2 sm:space-y-4`}
                >
                  <button
                    class="text-neutral font-bold text-lg sm:text-xl mb-2 cursor-pointer"
                    on:click={() => goto(`/creategoals/${goal.name}`)}
                  >
                    {goal.name}
                  </button>
                  <div class="text-sm sm:text-base text-gray-900 font-bold my-2">Details:</div>
                  <p class="text-gray-900"><strong>S:</strong> {goal.specific}</p>
                  <p class="text-gray-900"><strong>M:</strong> {goal.measurable}</p>
                  <p class="text-gray-900"><strong>A:</strong> {goal.attainable}</p>
                  <p class="text-gray-900"><strong>R:</strong> {goal.relevant}</p>
                  <p class="text-gray-900"><strong>T:</strong> {goal.timeBound}</p>
                  <div class="grid grid-cols-2 gap-2 text-xs sm:text-sm text-gray-500 mt-4">
                    <div><strong>Date for Completing Your SMART Goal:</strong></div>
                    <div>{goal.date}</div>
                    <div><strong>Days Your SMART Goal Repeats:</strong></div>
                    <div>
                      <DaysOfWeekSelector {daysOfWeek} readOnly={true} />
                      <div class="flex flex-row">
                        {#each goal.days as day}<span class="mx-1">{day}</span>{/each}
                      </div>
                    </div>
                    <div><strong>Time for Your SMART Goal Alert:</strong></div>
                    <div>{goal.time}</div>
                  </div>
                </div>
              {/each}
            {/if}
          </div>
        </div>
      {/each}
    </div>
  </div>
{/if}
