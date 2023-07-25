import { expect, test } from '@playwright/test';

test('page loads', async ({ page }) => {
  await page.goto('/signup');
  await expect(page.locator('#navbar')).toBeVisible();
});

test('required fields', async ({ page }) => {
  await page.goto('/signup');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#first-name-error')).toBeVisible({ timeout: 7000 });
  await expect(page.locator('#last-name-error')).toBeVisible({ timeout: 7000 });
  await expect(page.locator('#user-name-error')).toBeVisible({ timeout: 7000 });
  await expect(page.locator('#password-error')).toBeVisible({ timeout: 7000 });
});

test('not logged in buttons', async ({ page }) => {
  await page.goto('/signup');
  await expect(page.locator('#btn-sign-up')).toBeVisible({ timeout: 7000 });
  await expect(page.locator('#btn-save')).not.toBeVisible({ timeout: 7000 });
  await expect(page.locator('#btn-log-out')).not.toBeVisible({ timeout: 7000 });
  await expect(page.locator('#btn-delete')).not.toBeVisible({ timeout: 7000 });
});
