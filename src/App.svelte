<script lang="ts">
  import { Router, Route, Link } from "svelte-navigator";
  import Header from "./app/components/header/Header.svelte";
  import Footer from "./app/components/footer/Footer.svelte";
  import ChampionList from "./app/pages/champion-list/ChampionList.svelte";
</script>

<Header />
<Router>
  <nav class="nav">
    <div class="nav__decorator-wrapper">
      <div class="nav__el-wrapper">
        <div class="nav__el">
          <Link to="/">All</Link>
        </div>
      </div>

      <div class="nav__el-wrapper">
        <div class="nav__el">
          <Link to="assassins">Assassins</Link>
        </div>
      </div>

      <div class="nav__el-wrapper">
        <div class="nav__el">
          <Link to="fighters">Fighters</Link>
        </div>
      </div>

      <div class="nav__el-wrapper">
        <div class="nav__el">
          <Link to="mages">Mages</Link>
        </div>
      </div>

      <div class="nav__el-wrapper">
        <div class="nav__el">
          <Link to="marksmen">Marksmen</Link>
        </div>
      </div>

      <div class="nav__el-wrapper">
        <div class="nav__el">
          <Link to="supports">Supports</Link>
        </div>
      </div>

      <div class="nav__el-wrapper">
        <div class="nav__el">
          <Link to="tanks">Tanks</Link>
        </div>
      </div>
    </div>
  </nav>

  <div>
    <Route path="" primary={false}>
      <ChampionList listType="all" />
    </Route>

    <Route path="assassins" primary={false}>
      <ChampionList listType="assassins" />
    </Route>

    <Route path="fighters" primary={false}>
      <ChampionList listType="fighters" />
    </Route>

    <Route path="mages" primary={false}>
      <ChampionList listType="mages" />
    </Route>

    <Route path="marksmen" primary={false}>
      <ChampionList listType="marksmen" />
    </Route>

    <Route path="supports" primary={false}>
      <ChampionList listType="supports" />
    </Route>

    <Route path="tanks" primary={false}>
      <ChampionList listType="tanks" />
    </Route>
  </div>
</Router>
<Footer />

<style>
  .nav {
    background-color: white;
    justify-content: center;
    padding: 8px;
  }
  .nav__el-wrapper {
    background-color: transparent;
    padding-right: 4px;
    padding-left: 4px;
  }
  .nav__el {
    background-color: transparent;
    padding: 8px;
  }
  .nav__decorator-wrapper {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    border: 2px solid black;
  }
</style>
