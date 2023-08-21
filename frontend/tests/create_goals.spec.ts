import { expect, test } from '@playwright/test';
import { v4 as uuidv4 } from 'uuid';

test('page loads', async ({ page }) => {
  await page.goto('/create-goals');
  await expect(page.locator('#navbar')).toBeVisible();
});

test('goal is required', async ({ page }) => {
  await page.goto('/create-goals');
  await expect(page.locator('#goal')).toBeVisible();
  await page.locator('#save-goal-button').click();
  await expect(page.locator('#goal-error')).toBeVisible();
});

test('not logged in', async ({ page }) => {
  await page.goto('/create-goals');
  await expect(page).toHaveURL('/');
});

test('end to end create goal', async ({ page }) => {
  const userName = uuidv4();
  const password = 'mypassword';
  const securityAnswer = 'my answer';
  const goal = 'my goal';
  const specific = 'specific';
  const measurable = 'measurable';
  const achievable = 'achievable';
  const relevant = 'relevant';
  const timeBound = 'time bound';

  await page.goto('/');
  await expect(
    page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }),
  ).toBeVisible();
  await page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }).click();
  await expect(page.locator('#first-name')).toBeVisible();
  await expect(page.locator('#last-name')).toBeVisible();
  await expect(page.locator('#user-name')).toBeVisible();
  await expect(page.locator('#security-question-answer')).toBeVisible();
  await expect(page.locator('#password')).toBeVisible();
  await expect(page.locator('#verify-password')).toBeVisible();
  await expect(page.locator('#btn-sign-up')).toBeVisible();
  await page.locator('#first-name').fill('Imma');
  await page.locator('#last-name').fill('User');
  await page.locator('#user-name').fill(userName);
  await page.locator('#security-question-answer').fill(securityAnswer);
  await page.locator('#password').fill(password);
  await page.locator('#verify-password').fill(password);
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#btn-log-out')).toBeVisible();
  await page.getByLabel('create goals').click();
  await expect(page).toHaveURL('/create-goals');
  await expect(page.locator('#goal')).toBeVisible();
  await expect(page.locator('#specific')).toBeVisible();
  await expect(page.locator('#measurable')).toBeVisible();
  await expect(page.locator('#achievable')).toBeVisible();
  await expect(page.locator('#relevant')).toBeVisible();
  await expect(page.locator('#time-bound')).toBeVisible();
  await page.locator('#goal').fill(goal);
  await page.locator('#specific').fill(specific);
  await page.locator('#measurable').fill(measurable);
  await page.locator('#achievable').fill(achievable);
  await page.locator('#relevant').fill(relevant);
  await page.locator('#time-bound').fill(timeBound);
  await page.locator('#save-goal-button').click();
  await expect(page.locator('#toast-message')).toBeVisible();
  await expect(page).toHaveURL('/', { timeout: 10000 });

  await page.getByLabel('account settings').click();
  await expect(page.locator('#btn-delete')).toBeVisible();
  await page.once('dialog', async (dialog) => {
    await dialog.accept();
  });
  await page.locator('#btn-delete').click();
  await expect(page).toHaveURL('/');
});
