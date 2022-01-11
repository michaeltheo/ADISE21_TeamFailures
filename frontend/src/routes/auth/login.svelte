<script context="module">
	export async function load({ session }) {
		if (session.user) {
			return {
				status: 302,
				redirect: '/'
			};
		}
		return {};
	}
</script>

<script>
	import { session } from '$app/stores';
	import { goto } from '$app/navigation';

	// Variables bound to respective inputs via bind:value
	let username;
	let password;
	let error;
	let token;
	// let notice

	const login = async () => {
		// Reset error from previous failed attempts
		error = undefined;

		// POST method to src/routes/auth/login.js endpoint
		try {
			const res = await fetch('http://127.0.0.1:8000/Auth/login', {
				method: 'POST',
				body: new URLSearchParams({
					username,
					password
				}),
				headers: {
					'Content-Type': 'application/json',
					'Content-Type': 'application/x-www-form-urlencoded'
				}
			});

			if (res.ok) {
				const data = await res.json();
				$session.user = data.user;
				token = `Bearer ${data.access_token}`;
				$session.token = data.access_token;
				localStorage.setItem('FBidToken', token);
				goto('/');
			} else {
				const data = await res.json();
				error = `LOS001: ${data.message}`;
			}
		} catch (err) {
			console.log(err);
			error = 'LOS002: Pleas try it again.';
		}
	};
</script>

<section>
	<form on:submit|preventDefault={login}>
		<div class="heading">
			<a class="back" href="/"><i class="bi bi-arrow-left" /></a>
			<h2>Login</h2>
		</div>
		<input required name="email" placeholder="Enter your email" bind:value={username} />
		<input
			type="password"
			required
			name="password"
			placeholder="Enter your password"
			bind:value={password}
		/>
		{#if error}
			<p>{error}</p>
		{/if}
		<button type="submit">Login</button>
	</form>
</section>

<svelte:head>
	<title>Login</title>
</svelte:head>

<style>
	.heading {
		display: flex;
		align-items: center;
		margin-bottom: 10px;
	}

	h2 {
		width: 100%;
		text-align: center;
		margin-right: 24px;
	}

	.back {
		color: var(--sub-color);
		font-size: 24px;
		height: 24px;
	}
	.back:hover {
		color: var(--font-color);
	}

	button {
		background: rgb(101, 145, 255);
		color: #fff;
	}
</style>
