<!-- </div> -->
<script>
	import Button from '@smui/button';
	import { onMount } from 'svelte';
	import TopAppBar, { Row, Section, Title } from '@smui/top-app-bar';
	import IconButton, { Icon } from '@smui/icon-button';
	import { mdiWeatherNight, mdiWeatherSunny, mdiHome } from '@mdi/js';
	import { Svg } from '@smui/common/elements';

	let darkTheme = undefined;
	let prominent = false;
	let dense = false;
	let secondaryColor = false;
	// Show mobile icon and display menu
	let showMobileMenu = false;
	const navItems = [
		{ label: 'home', href: '/' },
		{ label: 'login', href: '/login' },
		{ label: 'register', href: '/register' }
	];
	// Mobile menu click event handler
	const handleMobileIconClick = () => (showMobileMenu = !showMobileMenu);
	// Media match query handler
	const mediaQueryHandler = (e) => {
		// Reset mobile state
		if (!e.matches) {
			showMobileMenu = false;
		}
	};
	// Attach media query listener on mount hook
	onMount(() => {
		const mediaListener = window.matchMedia('(max-width: 767px)');
		mediaListener.addListener(mediaQueryHandler);
	});
</script>

<svelte:head>
	{#if darkTheme === undefined}
		<!-- SMUI Styles -->
		<link rel="stylesheet" href="/smui.css" media="(prefers-color-scheme: light)" />
		<link rel="stylesheet" href="/smui-dark.css" media="screen and (prefers-color-scheme: dark)" />
	{:else if darkTheme}
		<link rel="stylesheet" href="/smui.css" />
		<link rel="stylesheet" href="/smui-dark.css" media="screen" />
	{:else}
		<link rel="stylesheet" href="/smui.css" />
	{/if}
</svelte:head>
<!-- <div class="flexy">   -->
<div class="top-app-bar-container flexor">
	<TopAppBar variant="static" {prominent} {dense} color={secondaryColor ? 'secondary' : 'primary'}>
		<Row>
			<Section>
				<IconButton class="material-icons" ripple={false}>
					<Icon component={Svg} viewBox="0 0 24 24">
						<path fill="currentColor" d={mdiHome} />
					</Icon>
				</IconButton>
				<Title>Name</Title>
			</Section>
			<Section align="mid" toolbar>
				<div class="inner">
					<div
						on:click={handleMobileIconClick}
						class={`mobile-icon${showMobileMenu ? ' active' : ''}`}
					>
						<div class="middle-line" />
					</div>

					<ul class={`navbar-list${showMobileMenu ? ' mobile' : ''}`}>
						{#each navItems as item}
							<li>
								<Button href={item.href}>
									{item.label}
								</Button>
							</li>
						{/each}
					</ul>
				</div>
			</Section>
			<Section align="end" toolbar>
				<IconButton on:click={() => (darkTheme = !darkTheme)} aria-label="switch">
					<Icon component={Svg} viewBox="0 0 24 24">
						<path fill="currentColor" d={darkTheme ? mdiWeatherSunny : mdiWeatherNight} />
					</Icon>
				</IconButton>
			</Section>
		</Row>
	</TopAppBar>
</div>

<div class="main-container">
	<slot />
</div>

<style>
	.top-app-bar-container {
		max-width: 100%;
		width: 100%;
		height: auto;
		border: 1px solid var(--mdc-theme-text-hint-on-background, rgba(0, 0, 0, 0.1));
		/* margin: 0 18px 18px 0; */
		background-color: var(--mdc-theme-background, #fff);

		overflow: hidden;
		display: inline-block;
	}
	.navbar-list {
		text-decoration: none;
	}

	@media (max-width: 480px) {
		.top-app-bar-container {
			margin-right: 0;
		}
	}

	.flexy {
		display: flex;
		flex-wrap: wrap;
	}

	.flexor {
		display: inline-flex;
		flex-direction: column;
	}

	nav {
		background-color: rgba(0, 0, 0, 0.8);
		font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
		height: 45px;
	}
	.inner {
		max-width: 980px;
		padding-left: 20px;
		padding-right: 20px;
		margin: auto;
		box-sizing: border-box;
		display: flex;
		align-items: center;
		height: 100%;
	}
	.mobile-icon {
		width: 25px;
		height: 14px;
		position: relative;
		cursor: pointer;
	}
	.mobile-icon:after,
	.mobile-icon:before,
	.middle-line {
		content: '';
		position: absolute;
		width: 100%;
		height: 2px;
		background-color: #fff;
		transition: all 0.4s;
		transform-origin: center;
	}
	.mobile-icon:before,
	.middle-line {
		top: 0;
	}
	.mobile-icon:after,
	.middle-line {
		bottom: 0;
	}
	.mobile-icon:before {
		width: 66%;
	}
	.mobile-icon:after {
		width: 33%;
	}
	.middle-line {
		margin: auto;
	}
	.mobile-icon:hover:before,
	.mobile-icon:hover:after,
	.mobile-icon.active:before,
	.mobile-icon.active:after,
	.mobile-icon.active .middle-line {
		width: 100%;
	}
	.mobile-icon.active:before,
	.mobile-icon.active:after {
		top: 50%;
		transform: rotate(-45deg);
	}
	.mobile-icon.active .middle-line {
		transform: rotate(45deg);
	}
	.navbar-list {
		display: none;
		width: 100%;
		justify-content: space-between;
		margin: 0;
		padding: 0 40px;
	}
	.navbar-list.mobile {
		background-color: rgba(0, 0, 0, 0.8);
		position: fixed;
		display: block;
		height: calc(100% - 55px);
		bottom: 0;
		left: 0;
	}
	.navbar-list li {
		list-style-type: none;
		position: relative;
	}
	.navbar-list li:before {
		content: '';
		position: absolute;
		bottom: 0;
		left: 0;
		width: 100%;
		height: 1px;
	}
	.navbar-list a {
		color: #fff;
		text-decoration: none;
		display: flex;
		height: 45px;
		align-items: center;
		padding: 0 10px;
		font-size: 13px;
	}
	@media only screen and (min-width: 520px) {
		.mobile-icon {
			display: none;
		}
		.navbar-list {
			display: flex;
			padding: 0;
		}
		.navbar-list a {
			display: inline-flex;
		}
	}
	.main-container {
		margin: 20px;
	}
</style>
