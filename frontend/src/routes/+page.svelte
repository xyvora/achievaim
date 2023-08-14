<script lang="ts">
  import { onMount } from 'svelte';
  import GoalCard from '$lib/components/GoalCard.svelte';
  import Message from '$lib/components/Message.svelte';
  import Input from '$lib/components/Input.svelte';
  import { LoginError } from '$lib/errors';
  import { accessToken, goals, isLoading, isLoggedIn, loadGoals } from '$lib/stores/stores';
  import { login } from '$lib/api';
  import type { GoalOutput } from '$lib/generated';
  import { GoalStatus } from '$lib/generated';

  interface UserLogin {
    userName: string;
    password: string;
  }

  let userLogin: UserLogin = {
    userName: '',
    password: '',
  };

  let activeGoals: GoalOutput[] | null = null;
  let completedGoals: GoalOutput[] | null = null;

  import { page } from '$app/stores';

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
    try {
      await loadGoals();
      setActiveCompleted();
    } catch (error) {
      genericError = true;
      genericErrorMessage =
        'An error occurred trying to connect to the sever. Please try again later.';
      isLoading.set(false);
      return;
    }
    userLogin.userName = '';
    userLogin.password = '';
    isLoading.set(false);
  }

  function setActiveCompleted() {
    if ($goals !== null) {
      for (let goal of $goals) {
        if (goal.status === GoalStatus.ACTIVE) {
          if (activeGoals !== null) {
            activeGoals.push(goal);
          } else {
            activeGoals = [goal];
          }
        } else if (goal.status === 'completed') {
          if (completedGoals !== null) {
            completedGoals.push(goal);
          } else {
            completedGoals = [goal];
          }
        }
      }
    }
  }

  onMount(async () => {
    activeGoals = null;
    completedGoals = null;

    if ($accessToken !== null) {
      await loadGoals();
    }
    setActiveCompleted();
  });
</script>

<div class="page-fade-in">
  {#if !$isLoggedIn}
    <div class="hero min-h-screen bg-base-200">
      <div
        class="flex flex-col lg:flex-row justify-around items-center lg:items-start hero-content"
      >
        <div class="text-center lg:text-left lg:w-1/2">
          <h1 class="text-5xl text-left font-bold">Smart Tracking Your Goals.</h1>
          <p class="py-6 text-left">
            Achiev𝘼𝙄m (pronounced "AchieveAim" or "uh-cheev-aim", IPA: /əˈtʃi:v eɪm/) is a
            sophisticated tool leveraging artificial intelligence to assist users in formulating,
            tracking, and accomplishing their goals using the SMART (Specific, Measurable,
            Achievable, Relevant, Time-bound) methodology. It refines users' goals for clarity and
            realism and integrates features for tracking progress, including customizable reminders.
            The app promotes consistent habits by enabling users to schedule daily reminders,
            creating an effective and efficient platform for personal and professional growth.
          </p>
        </div>
        <div class="card flex-shrink-0 w-full lg:w-1/3 max-w-sm shadow-lg bg-base-100">
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

              <Message
                messageId="generic-error"
                message={genericErrorMessage}
                showMessage={genericError}
                isError={true}
              />

              <div class="form-control">
                <a href="/forgot-password" class="label-text-alt link link-hover mt-4 mb-4"
                  >Forgot password?</a
                >
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
      <div class="md:flex md:space-x-4">
        <!-- Left Column -->
        <div class="md:w-1/2 md:mb-0 mb-4 md:pr-2">
          <h2 class="text-xl font-bold mb-2">Active</h2>
          {#if activeGoals}
            {#each activeGoals as goal}
              <GoalCard {goal} />
            {/each}
          {:else}
            <div class="card w-full bg-primary">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <div class="flex text-xl items-center space-x-2">
                    <span>No active goals. Click the plus button to get SMART goals.</span>
                    <a
                      href="create-goals"
                      class="text-base-200 hover:text-base-100 transition duration-300 flex items-center"
                    >
                      <svg
                        class="icon-pulse items-center m-3"
                        xmlns="http://www.w3.org/2000/svg"
                        width="20"
                        height="20"
                        fill="currentColor"
                        viewBox="0 0 16 16"
                      >
                        <path
                          d="M8 0a8 8 0 100 16A8 8 0 008 0zM4 7h3V4a1 1 0 012 0v3h3a1 1 0 010 2H9v3a1 1 0 01-2 0V9H4a1 1 0 010-2z"
                        />
                      </svg>
                    </a>
                  </div>
                </figcaption>
              </figure>
            </div>
          {/if}
        </div>

        <!-- Right Column -->
        <div class="md:w-1/2 md:ml-4 md:pl-2">
          <h2 class="text-xl font-bold mb-2">Completed</h2>

          {#if completedGoals}
            {#each completedGoals as goal}
              <GoalCard {goal} />
            {/each}
          {:else}
            <div class="card w-full bg-primary">
              <figure>
                <figcaption class="p-4 card-body flex flex-col">
                  <div class="flex text-xl items-center space-x-2">
                    <span>No completed goals</span>
                  </div>
                </figcaption>
              </figure>
            </div>
          {/if}
        </div>
      </div>
    </div>
  {/if}
</div>

<style>
  @keyframes pulse {
    0%,
    100% {
      transform: scale(0.75);
    }
    50% {
      transform: scale(1.25);
    }
  }

  .icon-pulse {
    animation: pulse 4s linear infinite;
  }
</style>
