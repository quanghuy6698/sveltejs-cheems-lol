<script lang="ts">
  import Champion from "../../components/champion/Champion.svelte";
  import { beforeUpdate, afterUpdate } from "svelte";

  export let listType: string;
  let champInfo;

  beforeUpdate(() => {
    switch (listType) {
      case "all":
        champInfo = {
          champImg:
            "https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt570145160dd39dca/5db05fa8347d1c6baa57be25/RiotX_ChampionList_aatrox.jpg",
          champName: "Aatrox",
        };
        break;
      case "assassins":
        champInfo = {
          champImg:
            "https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt80ff58fe809777ff/5db05fa8adc8656c7d24e7d6/RiotX_ChampionList_akali.jpg",
          champName: "Akali",
        };
        break;
      case "fighters":
        champInfo = {
          champImg:
            "https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt413fcd7681fe0773/5db05fb089fb926b491ed805/RiotX_ChampionList_camille.jpg",
          champName: "Camille",
        };
        break;
      case "mages":
        champInfo = {
          champImg:
            "https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt1259276b6d1efa78/5db05fa86e8b0c6d038c5ca2/RiotX_ChampionList_ahri.jpg",
          champName: "Ahri",
        };
        break;
      case "marksmen":
        champInfo = {
          champImg:
            "https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/bltdd84b33ec501c137/60f9ede33f40e5481e85c0c6/RiotX_ChampionList_akshan_v2.jpg",
          champName: "Akshan",
        };
        break;
      case "supports":
        champInfo = {
          champImg:
            "https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/bltbbe3ce0c0ae1305b/5db05fb23a326d6df6c0e7b3/RiotX_ChampionList_bard.jpg",
          champName: "Bard",
        };
        break;
      case "tanks":
        champInfo = {
          champImg:
            "https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt3b366925d2fd8fdb/5db05fa856458c6b3fc1750b/RiotX_ChampionList_alistar.jpg",
          champName: "Alistar",
        };
        break;
    }
  });
</script>

<div class="content">
  <Champion {champInfo} />
  <Champion {champInfo} />
  <Champion {champInfo} />
  <Champion {champInfo} />
  <Champion {champInfo} />
  <Champion {champInfo} />
  <Champion {champInfo} />
  <Champion {champInfo} />
  <Champion {champInfo} />
  <Champion {champInfo} />
  <Champion {champInfo} />
  <Champion {champInfo} />
</div>

<style>
  .content {
    width: 100%;
    background-color: white;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
  }
</style>
