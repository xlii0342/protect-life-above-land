<template>
  <div class="home">
    <PageHeader :youtubeEmbedUrl="youtubeEmbedUrl" />
    
    <main id="main-content">
      <section class="section">
        <ExtinctSpecies 
          :extinctSpecies="extinctSpecies" 
          @show-species-details="showSpeciesDetails" 
        />

        <EndangeredCategory 
          :criticallyEndangeredSpecies="criticallyEndangeredSpecies"
          :endangeredSpecies="endangeredSpecies"
          :vulnerableSpecies="vulnerableSpecies"
          @show-species-details="showSpeciesDetails"
        />

        <div class="chart-section-container">
          <button class="explore-button" @click="toggleChartVisibility">
            {{ showChart ? 'Hide Threatened Species Data' : 'Explore Threatened Species Data' }}
          </button>
          
          <transition name="fade">
            <div v-if="showChart" class="visualization-section">
              <h2>Explore Threatened Species</h2>
              <ThreatenedSpeciesChart :speciesData="speciesData" />
            </div>
          </transition>
        </div>

        <ActionSection />
      </section>

      <SpeciesModal 
        :species="selectedSpecies"
        @close-modal="closeModal"
      />
    </main>
    <Footer />
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import { useStore } from 'vuex'
import Footer from '@/components/Footer.vue'
import PageHeader from '@/components/home/PageHeader.vue'
import ExtinctSpecies from '@/components/home/ExtinctSpecies.vue'
import EndangeredCategory from '@/components/home/EndangeredCategory.vue'
import SpeciesModal from '@/components/home/SpeciesModal.vue'
import ActionSection from '@/components/home/ActionSection.vue'
import ThreatenedSpeciesChart from '@/components/home/ThreatenedSpeciesChart.vue'

export default {
  name: 'HomeView',
  components: {
    Footer,
    PageHeader,
    ExtinctSpecies,
    EndangeredCategory,
    SpeciesModal,
    ActionSection,
    ThreatenedSpeciesChart
  },
  setup() {
    const store = useStore()
    const selectedSpecies = ref(null)
    const youtubeVideoId = 'WnWm-zy5qKE'
    const showChart = ref(false)

    const toggleChartVisibility = () => {
      showChart.value = !showChart.value
    }

    const youtubeEmbedUrl = computed(() => {
      return `https://www.youtube.com/embed/${youtubeVideoId}?autoplay=1&mute=1&loop=1&playlist=${youtubeVideoId}&controls=0&showinfo=0&rel=0&modestbranding=1&iv_load_policy=3`
    })

    const speciesData = [
      { species_subgroup: 'Mammals', status: 'Critically Endangered', count: 2 },
      { species_subgroup: 'Mammals', status: 'Endangered', count: 2 },
      { species_subgroup: 'Mammals', status: 'Vulnerable', count: 0 },
      { species_subgroup: 'Birds', status: 'Critically Endangered', count: 3 },
      { species_subgroup: 'Birds', status: 'Endangered', count: 1 },
      { species_subgroup: 'Birds', status: 'Vulnerable', count: 1 },
      { species_subgroup: 'Amphibians', status: 'Critically Endangered', count: 0 },
      { species_subgroup: 'Amphibians', status: 'Endangered', count: 0 },
      { species_subgroup: 'Amphibians', status: 'Vulnerable', count: 1 }
    ]

    const speciesList = [
      {
        name: "Eastern Bettong",
        img: "https://upload.wikimedia.org/wikipedia/commons/3/3d/Bettongia_gaimardi.jpg",
        description: "Bettongs usually weigh around 2 kilograms and have a yellowish-grey coat on top with a white underside. Their tail is about the same length as their head and body combined, which sets them apart from potoroos, whose tails are noticeably shorter.",
        distribution: "The bettong lives in eastern Tasmania on islands like Maria and Bruny. It once lived on mainland Australia, including Victoria, but disappeared because of feral cats. Bettongs are small, nocturnal animals, making them easy targets for cats, which are skilled night hunters. With few safe places to hide, bettongs in Victoria were hunted to extinction by feral cats.",
        status: "Extinct"
      },
      {
        name: "Spot-tailed Quoll",
        img: "https://assets.wwf.org.au/image/upload/RSwwfau_16027_RSwwfau_16027",
        description: "The Spot-tailed Quoll is about the size of a domestic cat, but with shorter legs and a more pointed face. Its fur is a rich red to dark brown, covered with white spots that continue along its tail, making it easy to tell apart from other Australian animals. Males weigh around 3.5 kilograms, while females are about 2 kilograms",
        distribution: "The Spot-tailed Quoll lives along the Great Dividing Range, from Victoria to Queensland, in forests, woodlands, and rocky areas. In Victoria, it is endangered, with strongholds in East Gippsland and the Upper Snowy River. Feral cats threaten the quoll by hunting young quolls and competing for food, adding to the pressure from habitat loss",
        status: "Endangered"
      },
      {
        name: "Black-eared Miner",
        img: "https://live-production.wcms.abc-cdn.net.au/c84d05b9098340f279a981825d31b15a?impolicy=wcms_crop_resize&cropH=3127&cropW=4691&xPos=0&yPos=0&width=862&height=575",
        description: "The Black-eared Miner is a large honeyeater, about 23 to 26 centimetres long, with dark grey feathers above, paler below, and a bold black face mask. It looks like the Yellow-throated Miner but has a darker rump and no pale band on its tail.",
        distribution: "The Black-eared Miner is found in Victoria's mallee woodlands, mainly in the Murray-Sunset, Hattah-Kulkyne, and Wyperfeld National Parks. It is listed as critically endangered and feral cats as major threats. Feral cats hunt adult birds and chicks, and as mallee habitats shrink, the birds have fewer safe places to nest and feed.",
        status: "Critically Endangered"
      },
      {
        name: "Orange-bellied Parrot",
        img: "https://i0.wp.com/www.australiangeographic.com.au/wp-content/uploads/2021/02/H83TRA-scaled.jpg?fit=2560%2C1707&ssl=1",
        description: "The Orange-bellied Parrot is slightly larger than a budgerigar, about 23 cm long. Both males and females have greyish-black bills and brown eyes, but males are brighter, with grass-green feathers, bright yellow underparts, and a vivid orange belly patch. Males also have a deep blue band between the eyes and bright blue on the wings, while females are duller with less blue and a smaller orange patch.",
        distribution: "The critically endangered Orange-bellied Parrot, a small migratory parrot, breeds in Tasmania and migrates to coastal Victoria and South Australia for winter, relying on saltmarsh habitat for survival. Feral cats threaten the species by preying on birds during migration and at nesting sites.",
        status: "Critically Endangered"
      },
      {
        name: "Eastern Barred Bandicoot",
        img: "https://shop.zoo.org.au/cdn/shop/products/HC6235new.jpg?v=1629947894",
        description: "The Eastern Barred Bandicoot is a small, rabbit-sized marsupial with soft grey-brown fur and pale bars across its back and rump. It has a pointed snout, large ears, and a short tail. This bandicoot is mostly active at night, using its strong claws to dig for insects and plant roots. During the day, it hides in nests made of grass and leaves to stay safe from predators.",
        distribution: "Eastern Barred Bandicoots were once widespread across the grasslands and grassy woodlands of western Victoria, extending into south-eastern South Australia. Today, they survive only in small protected areas, as feral cats have heavily preyed on them, making the species highly vulnerable in the wild.",
        status: "Endangered"
      },
      {
        name: "Brush-tailed Rock-wallaby",
        img: "https://media.australian.museum/media/dd/images/Some_image.1340303c.fill-600x400.1c7f72a.jpg",
        description: "The Brush-tailed Rock-wallaby has a long, bushy tail that is darker and fluffier at the tip. Its thick brown fur is reddish on the rump and grey on the shoulders, with paler fur on the chest and belly. Some have a white blaze on their chest, along with a white stripe on the cheek and a black line from the forehead to the neck. Highly agile, this wallaby moves easily over rocky ground, using its strong build, flexible tail for balance, and rough-textured feet for grip. Males weigh about 8 kg and females around 6 kg.",
        distribution: "In Victoria, the Brush-tailed Rock-wallaby survives in only two small, isolated locations, with fewer than 60 animals left in the wild. This agile species lives in rugged, rocky areas, hiding among ridges during the day and feeding on grasses at dusk. Feral cats are a major threat, preying on young wallabies and adding pressure to the already fragile population.",
        status: "Critically Endangered"
      },
      {
        name: "Bolam's Mouse",
        img: "https://www.bushheritage.org.au/cdn-cgi/image/quality=90,format=auto,width=800,gravity=0.5x0.5,fit=scale-down/https://www.bushheritage.org.au/uploads/main/Images/News/2020/Scats-used-to-find-what/The-Desert-short-tailed-mouse-is-known-to-live-on-Bon-Bon-Station-Reserve-its-remains-having-recently-been-discovered-in-fox-scats.jpg",
        description: "Bolam's Mouse is a small rodent, weighing between 9 and 21 grams, with a body length of 5 to 8 centimetres and a long, furry tail. Its fur is dull amber-brown to olive-brown on top and white underneath. It has large ears, big eyes, and looks like a House Mouse but with a longer tail, bigger ears, and no musty smell.",
        distribution: "Bolam's Mouse used to live in the semi-arid woodlands and shrublands of north-western Victoria. Today, it is considered extinct in Victoria, with populations surviving only in parts of South Australia and Western Australia. Feral cats were a major threat, hunting these small mice and contributing to their disappearance from Victoria.",
        status: "Extinct"
      },
      {
        name: "Desert Mouse",
        img: "https://www.australianwildlife.org/sites/default/files/media/image/2025-01/Dusky%20Hopping%20Mouse-4.jpg",
        description: "The Desert Mouse is a small rodent with bright chestnut-brown fur and dark, spiky guard hairs that give it a rough look. It has a brown, scaly tail that is about the same length as its body. The mouse has big eyes with a pale orange ring around them, and its underparts are greyish-white. Both males and females are similar in size, weighing between 11 and 35 grams.",
        distribution: "In Victoria, the Desert Mouse once lived in sandy deserts and dry woodland areas of the northwest. It is now extinct in the state, with feral cats contributing to its decline by preying on these small, ground-dwelling rodents. The loss of habitat and predation pressures forced the Desert Mouse to disappear from Victoria's wild landscapes.",
        status: "Extinct"
      },
      {
        name: "Western Whipbird (Mallee)",
        img: "https://birdlife.org.au/wp-content/uploads/2022/12/Western-Whipbird-immature-Tom-Hunt.jpg",
        description: "The Mallee Whipbird is a medium-sized bird, about 20–25 cm long, weighing around 47 grams. It has a short crest, a dark grey bill, long grey legs, and a long tail. Its feathers are grey to olive, with a white stripe down each cheek and along the belly, and a black chin and throat. It also has dull red eyes, with a thin grey ring around them.",
        distribution: "In Victoria, the Mallee Whipbird is critically endangered and found only in small, isolated patches of mallee vegetation in the northwest. It depends on dense shrubland for shelter and nesting. Feral cats are a serious threat, preying on these secretive birds and making it harder for the population to recover in the wild.",
        status: "Critically Endangered"
      },
      {
        name: "Mallee Emu-wren",
        img: "https://i0.wp.com/www.australiangeographic.com.au/wp-content/uploads/2024/10/Mallee-Emu-wren_adjusted-scaled-e1730099610660.jpg?fit=1800%2C1259&ssl=1",
        description: "The Mallee Emu-wren is a tiny bird, about 10–15 cm long, with a very fine, long tail made of wispy feathers that look like emu feathers. Its body is warm brown above and pale underneath, with soft streaking. Males have a bright orange-brown body and a blue throat and eyebrow stripe. Females are plainer, without the blue markings. Despite their small size, they move quickly through dense mallee shrubs.",
        distribution: "In Victoria, the Mallee Emu-wren is endangered and found only in a few remaining areas of mallee vegetation in the northwest. It depends on dense, spinifex grass for shelter and nesting. Feral cats are a major threat, as they hunt these tiny birds in their ground-level habitat, making it even harder for the species to survive.",
        status: "Endangered"
      },
      {
        name: "Malleefowl",
        img: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Malleefowl_0A2A4564.jpg/330px-Malleefowl_0A2A4564.jpg",
        description: "The Malleefowl is a large ground-dwelling bird, growing up to 60 cm long and weighing around 2.5 kg. Its head and neck are buff-grey, and its body is a mix of brown, black, and white, helping it blend into the environment. With sharp hearing and eyesight, the Malleefowl can sense danger early and usually sneaks away, relying on its camouflage. Though it can fly well, it prefers to run quickly when startled.",
        distribution: "In Victoria, the Malleefowl is listed as vulnerable and mainly found in the dry mallee woodlands of the northwest. It relies on sandy soils and dense shrubs for nesting and food. Feral cats are a major threat, preying on both adult birds and chicks, making it harder for the species to survive in the wild.",
        status: "Vulnerable"
      },
      {
        name: "Growling Grass Frog",
        img: "https://gtsag.org.au/wp-content/uploads/2024/05/Growling-Grass-Frog-by-Dave-Newman.jpg",
        description: "The Growling Grass Frog, also called the Southern Bell Frog, is one of Australia's largest frogs, growing up to 10 cm long. They live in south-eastern Australia, often found in and around swamps and wetlands. At night, they move between wet areas in search of food. These frogs are patient predators, feeding on insects, small lizards, fish, tadpoles, and even other frogs.",
        distribution: "In Victoria, the Growling Grass Frog is listed as vulnerable and lives in wetlands, swamps, and lagoons across the state. These frogs need healthy, connected wetlands to move between, especially during rainy nights. Feral cats are a major threat, preying on young frogs and adding pressure to their shrinking populations.",
        status: "Vulnerable"
      },
      {
        name: "Southern Bent-wing Bat",
        img: "https://live-production.wcms.abc-cdn.net.au/b6d2cd28ecd904fde491608e70c82a39?impolicy=wcms_crop_resize&cropH=1212&cropW=2154&xPos=0&yPos=98&width=862&height=485",
        description: "The Southern Bent-wing Bat is an insect-eating, cave-dwelling bat with dark reddish-brown to dark brown fur. Its belly is slightly lighter, and it has a short, rounded face with a domed head. The bat's ears are short and triangular, and its long, curved wing bones give it a distinctive bent-wing shape.",
        distribution: "In Victoria, the Southern Bent-wing Bat is critically endangered and survives only in a few limestone caves in the southwest. These bats depend on safe, undisturbed caves to roost and raise their young. Feral cats are a major threat, hunting bats as they enter and leave their roosts, putting extra pressure on this small population.",
        status: "Critically Endangered"
      }
    ]

    // 计算属性：过滤出已灭绝的物种
    const extinctSpecies = computed(() => {
      return speciesList.filter(species => species.status === 'Extinct')
    })

    // 计算属性：过滤出极度濒危物种
    const criticallyEndangeredSpecies = computed(() => {
      return speciesList.filter(species => species.status === 'Critically Endangered')
    })

    // 计算属性：过滤出濒危物种
    const endangeredSpecies = computed(() => {
      return speciesList.filter(species => species.status === 'Endangered')
    })

    // 计算属性：过滤出易危物种
    const vulnerableSpecies = computed(() => {
      return speciesList.filter(species => species.status === 'Vulnerable')
    })

    const showSpeciesDetails = (species) => {
      selectedSpecies.value = species
      store.dispatch('setSelectedSpecies', species)
    }

    const closeModal = () => {
      selectedSpecies.value = null
      store.dispatch('setSelectedSpecies', null)
    }

    return {
      speciesList,
      extinctSpecies,
      criticallyEndangeredSpecies,
      endangeredSpecies,
      vulnerableSpecies,
      selectedSpecies,
      showSpeciesDetails,
      closeModal,
      youtubeVideoId,
      youtubeEmbedUrl,
      speciesData,
      showChart,
      toggleChartVisibility
    }
  }
}
</script>

<style scoped>
.home {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  position: relative;
}

/* 内容区域样式 */
main {
  flex: 1;
  position: relative;
  z-index: 1;
  background-color: #f9f9f9;
  padding: 2rem 1rem;
  background-image: linear-gradient(to bottom, #f5f9f8, #f9f9f9);
}

.section {
  background-color: transparent;
  margin: 0 auto 3rem;
  max-width: 1200px;
  padding: 0;
  position: relative;
}

/* 确保各子部分之间有足够间距 */
.section > * {
  margin-bottom: 2rem;
}

.section > *:last-child {
  margin-bottom: 0;
}

/* Visualization section styles */
.visualization-section {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  padding: 25px;
  margin: 0 0 60px 0;
  position: relative;
  z-index: 1;
  border-bottom: 1px solid #e0e0e0;
  min-height: 550px;
  width: 100%;
  transition: all 0.5s ease;
}

.visualization-section h2 {
  text-align: center;
  margin-bottom: 25px;
  color: #2c3e50;
  font-size: 1.8rem;
}

.visualization-section::after {
  content: '';
  display: block;
  height: 30px;
  width: 100%;
  position: absolute;
  bottom: -30px;
}

@media (max-width: 992px) {
  .section {
    padding: 0;
  }
  
  .visualization-section {
    padding: 15px;
    margin: 30px 0 100px 0;
  }
}

.chart-section-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px 0;
}

.explore-button {
  background-color: #3a6659;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 50px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.explore-button:hover {
  background-color: #2c4f46;
  transform: translateY(-2px);
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}

.explore-button:active {
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s, transform 0.5s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}
</style> 