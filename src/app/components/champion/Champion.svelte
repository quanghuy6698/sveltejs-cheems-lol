<script lang="ts">
</script>

<div class="champion">
  <div class="champion__content-wrapper">
    <div class="row">
      <div class="col-4">
        <img
          alt="champion"
          src="https://lmtocchien.com/wp-content/uploads/2021/02/cach-choi-akali-toc-chien.jpg"
          class="champion__img"
        />
      </div>
      <div class="col-8 champion__name">
        <span>Akali</span>
      </div>
    </div>
    <div class="champion__intro-wrapper">
      <p class="champion__intro">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in enim sit
        amet diam vestibulum cursus. Maecenas blandit lobortis ex, non laoreet
        nulla viverra et. Cras vel iaculis urna, non condimentum mauris.
        Phasellus quis leo at lectus fringilla hendrerit.
      </p>
    </div>
  </div>
</div>

<style>
  .champion {
    background-color: transparent;
    width: 300px;
    height: 300px;
    padding: 4px;
  }

  .champion__content-wrapper {
    background-color: aqua;
    width: 276px;
    height: 276px;
    border-top-left-radius: 8px;
    border-bottom-left-radius: 22px;
    border-top-right-radius: 22px;
    padding: 8px;
    box-shadow: 2px 2px #808080;
  }

  .champion__img {
    width: 50px;
    height: 50px;
    border-radius: 8px;
  }

  .champion__intro-wrapper {
    width: 100%;
    height: 100%;
  }

  .champion__intro {
    text-overflow: ellipsis;
  }

  .champion__name {
    background-color: tomato;
    border-radius: 4px;
    color: cornsilk;
    font-size: 24px;
  }
</style>
