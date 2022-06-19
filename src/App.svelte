<script lang="ts">
  import { Router, Route, Link } from "svelte-navigator";
  import Header from "./app/components/header/Header.svelte";
  import Footer from "./app/components/footer/Footer.svelte";
  import Home from "./app/pages/home/Home.svelte";
</script>

<Header />
<Router>
  <nav class="nav">
    <div class="nav__el-wrapper">
      <div class="nav__el">
        <Link to="/">Home</Link>
      </div>
    </div>
    <div class="nav__el-wrapper">
      <div class="nav__el">
        <Link to="maskman">Maskman</Link>
      </div>
    </div>
    <div class="nav__el-wrapper">
      <div class="nav__el">
        <Link to="mage">Mage</Link>
      </div>
    </div>
  </nav>
  <div>
    <Route path="" primary={false}>
      <Home />
    </Route>

    <Route path="maskman" primary={false}>maskman</Route>

    <Route path="mage" primary={false}>mage</Route>
  </div>
</Router>
<Footer />

<style>
  .nav {
    background-color: springgreen;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    /* padding-top: 8px;
    padding-bottom: 8px; */
  }
  .nav__el-wrapper {
    background-color: transparent;
    padding-right: 4px;
    padding-left: 4px;
  }
  .nav__el {
    background-color: royalblue;
    padding: 8px;
  }
</style>
