<template>
  <div class="home">
    <main>
      <section class="sdg-section">
        <img src="https://agriculture.vic.gov.au/__data/assets/image/0009/642429/AndrewCooke-FeralCat.jpeg" alt="Feral Cat">
        <div class="sdg-text">
          <h2>Feral Cats are Destroying Biodiversity</h2>
          <p>Learn about the native species most at risk — and take action to protect them!</p>
          <p><strong>Support SDG-15: Life on Land</strong></p>
          <button class="read-more-btn" @click="toggleSDG">Click here to read more</button>
          <div class="sdg-details" :class="{ show: showSDG }">
            <p><strong>SDG 15</strong> is about protecting, restoring and promoting sustainable use of terrestrial ecosystems and biodiversity. In Victoria, feral cats kill millions of native animals each year.</p>
            <p>This includes threatened species like the Malleefowl, Eastern Bettong, and Spot-tailed Quoll — many of which are already on the edge of extinction.</p>
            <p>You can support SDG-15 by reporting sightings, encouraging responsible pet ownership, and spreading awareness.</p>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>Do You Know These Endangered Species?</h2>
        <div class="grid">
          <div v-for="species in speciesList" :key="species.name" class="card" @click="showSpeciesDetails(species)">
            <img :src="species.img" :alt="species.name">
            <p>{{ species.name }}</p>
          </div>
        </div>
        <h2>You Can Make a Difference</h2>
        <div class="actions">
          <router-link to="/pet-owner" class="action-button">
            <button class="cat-owner-btn">Cat Owner Info</button>
          </router-link>
          <router-link to="/community" class="action-button">
            <button>Community</button>
          </router-link>
        </div>
        <div class="map-placeholder">🗺 Interactive Map of Victoria – Coming Soon</div>
      </section>

      <div class="overlay" :class="{ active: selectedSpecies }" @click="closeModal">
        <div class="modal" @click.stop>
          <button class="close-btn" @click="closeModal">X</button>
          <img v-if="selectedSpecies" :src="selectedSpecies.img" :alt="selectedSpecies.name">
          <h3 v-if="selectedSpecies">{{ selectedSpecies.name }}</h3>
          <div v-if="selectedSpecies">
            <p>{{ selectedSpecies.description }}</p>
            <h3>Distribution & Habitat</h3>
            <p>{{ selectedSpecies.distribution }}</p>
            <h3>Population Status In Victoria</h3>
            <div class="status-scale">
              <span class="status-item" :class="{ active: selectedSpecies.status === 'Vulnerable' }">Vulnerable</span>
              <span class="status-item" :class="{ active: selectedSpecies.status === 'Endangered' }">Endangered</span>
              <span class="status-item" :class="{ active: selectedSpecies.status === 'Critically Endangered' }">Critically Endangered</span>
              <span class="status-item" :class="{ active: selectedSpecies.status === 'Extinct', 'extinct-status': selectedSpecies.status === 'Extinct' }">Extinct</span>
            </div>
          </div>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import Footer from '@/components/Footer.vue'

export default {
  name: 'HomeView',
  components: {
    Footer
  },
  setup() {
    const store = useStore()
    const showSDG = ref(false)
    const selectedSpecies = ref(null)

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
        img: "https://images.ala.org.au/image/proxyImageThumbnail?imageId=564d580b-6d8f-435f-99d3-f0c74dd1fb50",
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

    const toggleSDG = () => {
      showSDG.value = !showSDG.value
    }

    const showSpeciesDetails = (species) => {
      selectedSpecies.value = species
      store.dispatch('setSelectedSpecies', species)
    }

    const closeModal = () => {
      selectedSpecies.value = null
      store.dispatch('setSelectedSpecies', null)
    }

    return {
      showSDG,
      speciesList,
      selectedSpecies,
      toggleSDG,
      showSpeciesDetails,
      closeModal
    }
  }
}
</script>

<style scoped>
.home {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1;
}

.sdg-section {
  display: flex;
  flex-wrap: wrap;
  padding: 2rem;
  background: white;
  max-width: 1200px;
  margin: 2rem auto;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.sdg-section img {
  flex: 1;
  max-width: 400px;
  width: 100%;
  border-radius: 10px;
  object-fit: cover;
}

.sdg-text {
  flex: 2;
  padding: 1rem 2rem;
}

.sdg-text h2 {
  color: #2f4f4f;
  margin-bottom: 1rem;
  font-size: 1.8rem;
}

.sdg-text p {
  margin-bottom: 1rem;
  font-size: 1.05rem;
}

.read-more-btn {
  background-color: #fcd34d;
  border: none;
  padding: 0.6rem 1.2rem;
  font-weight: bold;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.read-more-btn:hover {
  background-color: #fbbf24;
}

.sdg-details {
  display: none;
  margin-top: 1rem;
  background: #f1f1f1;
  padding: 1rem;
  border-radius: 8px;
  line-height: 1.6;
  font-size: 0.95rem;
}

.sdg-details.show {
  display: block;
}

.section {
  padding: 2rem;
  max-width: 1200px;
  margin: auto;
}

.section h2 {
  color: #2f4f4f;
  font-size: 1.6rem;
  margin-bottom: 1rem;
  text-align: center;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem;
  justify-items: center;
}

.card {
  background: white;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
  cursor: pointer;
  transition: transform 0.3s ease;
  width: 100%;
  max-width: 250px;
}

.card:hover {
  transform: scale(1.03);
}

.card img {
  width: 100%;
  height: 150px;
  object-fit: cover;
}

.card p {
  padding: 0.75rem;
  text-align: center;
  font-weight: 600;
}

.actions {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin: 2rem 0;
}

.action-button {
  text-decoration: none;
}

.action-button button {
  padding: 0.8rem 1.5rem;
  font-size: 1.1rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: #4CAF50;
  color: white;
  font-weight: 600;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.action-button button:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  background-color: #45a049;
}

.cat-owner-btn {
  background-color: #3a6659 !important;
}

.cat-owner-btn:hover {
  background-color: #2c4f46 !important;
}

.map-placeholder {
  margin-top: 3rem;
  height: 250px;
  background: #ddd;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  border-radius: 10px;
}

.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(5px);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 100;
}

.overlay.active {
  display: flex;
}

.modal {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  width: 90%;
  max-width: 600px;
  position: relative;
  box-shadow: 0 4px 20px rgba(0,0,0,0.25);
  max-height: 85vh;
  overflow-y: auto;
}

.modal img {
  width: 100%;
  height: 320px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 1rem;
}

.modal h3 {
  margin-bottom: 0.5rem;
  color: #2f4f4f;
}

.modal p {
  margin-bottom: 1rem;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 14px;
  background: #2f4f4f;
  color: white;
  border: none;
  font-size: 1.2rem;
  padding: 0.2rem 0.6rem;
  border-radius: 50px;
  cursor: pointer;
  z-index: 200;
  transition: background 0.3s ease;
}

.close-btn:hover {
  background: #1e3838;
}

.status-scale {
  display: flex;
  justify-content: flex-start;
  margin: 1rem 0;
  background: #f5f5f5;
  border-radius: 5px;
  padding: 0.5rem;
  flex-wrap: nowrap;
  white-space: nowrap;
  overflow-x: auto;
}

.status-item {
  padding: 0.5rem 0.8rem;
  border-radius: 4px;
  font-size: 0.9rem;
  opacity: 0.6;
  text-align: center;
  font-weight: 600;
  margin-right: 0.5rem;
  display: inline-block;
}

.status-item:last-child {
  margin-right: 0;
}

.status-item.active {
  background: #d32f2f;
  color: white;
  opacity: 1;
}

.extinct-status.active {
  background: #d32f2f !important;
}
</style> 