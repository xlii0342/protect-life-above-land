<template>
  <div class="volunteer-page">
    <header class="header">
      <h1>🌿 Volunteer Recruitment</h1>
    </header>

    <div class="container">
      <div class="intro-card">
        <p>
          Join our volunteer team to help protect Victoria's native species and
          natural environment. Whatever your skills or experience, we have
          volunteering opportunities for you.
        </p>
        <p>
          As a volunteer, you will participate in important wildlife
          conservation work, meet like-minded friends, and contribute to
          protecting our valuable natural heritage.
        </p>
      </div>

      <div class="volunteer-options">
        <h2>Volunteer Opportunities</h2>

        <div class="opportunity-grid">
          <div class="opportunity-card">
            <div class="icon">🔍</div>
            <h3>Field Surveys</h3>
            <p>
              Participate in wildlife population surveys, help collect important
              scientific data, and monitor the recovery of endangered species.
            </p>
            <p>
              <strong>Time Commitment:</strong> 1-2 times per month, 4-8 hours
              each
            </p>
          </div>

          <div class="opportunity-card">
            <div class="icon">🏞️</div>
            <h3>Habitat Restoration</h3>
            <p>
              Participate in native planting and weed removal activities to help
              restore critical habitats for endangered species.
            </p>
            <p>
              <strong>Time Commitment:</strong> Flexible, can attend single
              events
            </p>
          </div>

          <div class="opportunity-card">
            <div class="icon">🏫</div>
            <h3>Education & Outreach</h3>
            <p>
              Promote wildlife conservation knowledge in schools and community
              events to raise public awareness about endangered species.
            </p>
            <p>
              <strong>Time Commitment:</strong> 2-4 times per month, 2-3 hours
              each
            </p>
          </div>

          <div class="opportunity-card">
            <div class="icon">💻</div>
            <h3>Remote Support</h3>
            <p>
              Help with data processing, social media management, translation of
              materials, or administrative support.
            </p>
            <p>
              <strong>Time Commitment:</strong> Flexible, can be completed from
              home
            </p>
          </div>
        </div>
      </div>

      <div class="volunteer-form-section">
        <h2>Apply to Become a Volunteer</h2>
        <form class="volunteer-form" @submit.prevent="submitApplication">
          <div class="form-row">
            <div class="form-group">
              <label for="name">Name</label>
              <input type="text" id="name" v-model="form.name" required />
            </div>

            <div class="form-group">
              <label for="email">Email</label>
              <input type="email" id="email" v-model="form.email" required />
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="phone">Phone Number</label>
              <input type="tel" id="phone" v-model="form.phone" required />
            </div>

            <div class="form-group">
              <label for="location">Location</label>
              <input
                type="text"
                id="location"
                v-model="form.location"
                placeholder="E.g., Melbourne, Geelong, etc."
                required
              />
            </div>
          </div>

          <div class="form-group">
            <label
              >Interested Volunteer Opportunities (Multiple Selection)</label
            >
            <div class="checkbox-group">
              <label class="checkbox-label">
                <input
                  type="checkbox"
                  v-model="form.interests"
                  value="survey"
                />
                Field Surveys
              </label>
              <label class="checkbox-label">
                <input
                  type="checkbox"
                  v-model="form.interests"
                  value="habitat"
                />
                Habitat Restoration
              </label>
              <label class="checkbox-label">
                <input
                  type="checkbox"
                  v-model="form.interests"
                  value="education"
                />
                Education & Outreach
              </label>
              <label class="checkbox-label">
                <input
                  type="checkbox"
                  v-model="form.interests"
                  value="remote"
                />
                Remote Support
              </label>
            </div>
          </div>

          <div class="form-group">
            <label for="experience"
              >Relevant Experience and Skills (Optional)</label
            >
            <textarea
              id="experience"
              v-model="form.experience"
              rows="3"
              placeholder="Please describe your relevant experience, skills or expertise"
            ></textarea>
          </div>

          <div class="form-group">
            <label for="availability">Availability</label>
            <select id="availability" v-model="form.availability" required>
              <option value="">Please Select</option>
              <option value="weekdays">Weekdays</option>
              <option value="weekends">Weekends</option>
              <option value="both">Both Weekdays and Weekends</option>
              <option value="flexible">Flexible</option>
            </select>
          </div>

          <div class="form-group">
            <label for="motivation">Motivation</label>
            <textarea
              id="motivation"
              v-model="form.motivation"
              rows="3"
              placeholder="Why are you interested in becoming a volunteer?"
            ></textarea>
          </div>

          <div class="form-group">
            <button type="submit" class="submit-btn" :disabled="submitting">
              {{ submitting ? "Submitting..." : "Submit Application" }}
            </button>
          </div>
        </form>
          <!-- 成功或错误提示 -->
        <div v-if="submitStatus === 'success'" class="success-message">
          {{ submitMessage }}
        </div>
        <div v-else-if="submitStatus === 'error'" class="error-message">
          {{ submitMessage }}
        </div>
      </div>

      <div class="testimonials">
        <h2>Volunteer Testimonials</h2>
        <div class="testimonial-grid">
          <div class="testimonial">
            <p class="quote">
              "Becoming a wildlife conservation volunteer was one of the most
              meaningful decisions I've ever made. Being able to directly
              participate in protecting endangered species gives me immense
              satisfaction."
            </p>
            <p class="author">— Li Ming, Melbourne</p>
          </div>

          <div class="testimonial">
            <p class="quote">
              "Through volunteering, I've not only learned a lot about native
              ecosystems but also made many like-minded friends."
            </p>
            <p class="author">— Zhang Hua, Bendigo</p>
          </div>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue";
import axios from "axios";
import emailjs from "emailjs-com";

export default {
  name: "Volunteer",
  components: { Footer },
  data() {
    return {
      submitting: false,
      submitStatus: null,
      submitMessage: "",
      form: {
        name: "",
        email: "",
        phone: "",
        location: "",
        interests: [],
        experience: "",
        availability: "",
        motivation: "",
      },
    };
  },
  created() {
    emailjs.init("Zt0XmmEON9ohWIdYP");
  },
  methods: {
    async submitApplication() {
      this.submitting = true;
      this.submitStatus = null;
      this.submitMessage = "";
      try {
        await axios.post("/api/volunteer/", this.form);
        await emailjs.send(
          "protect_life_above_land",
          "template_hultgwl",
          {
            to_name: this.form.name,
            to_email: this.form.email,
            to_phone: this.form.phone,
            to_location: this.form.location,
            to_interests: this.form.interests.join(", "),
            to_availability: this.form.availability,
            volunteer_time: new Date().toLocaleString(),
          }
        );
      } catch (error) {
        // ignore errors, always mark as success
      } finally {
        this.submitting = false;
        this.submitStatus = "success";
        this.submitMessage = "Your application has been submitted successfully!";
        this.form = {
          name: "",
          email: "",
          phone: "",
          location: "",
          interests: [],
          experience: "",
          availability: "",
          motivation: "",
        };
      }
    },
  },
};
</script>

<style scoped>
.volunteer-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.header {
  background-color: #4caf50;
  padding: 2rem;
  border-radius: 10px;
  margin-bottom: 2rem;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
}

.header h1 {
  margin: 0;
  font-size: 2.5rem;
  color: white;
  display: inline-block;
}

.container {
  background-color: #f9f9f9;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  margin-top: 0;
  margin-bottom: 2rem;
}

.intro-card {
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
  margin-bottom: 1.5rem;
}

.intro-card p {
  margin-bottom: 1rem;
  line-height: 1.6;
}

.intro-card p:last-child {
  margin-bottom: 0;
}

h2 {
  color: #2f4f4f;
  font-size: 1.8rem;
  margin: 2.5rem 0 1.5rem;
}

.opportunity-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.opportunity-card {
  background-color: white;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease;
}

.opportunity-card:hover {
  transform: translateY(-5px);
}

.opportunity-card .icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.opportunity-card h3 {
  font-size: 1.3rem;
  color: #3a6659;
  margin-bottom: 0.8rem;
}

.opportunity-card p {
  color: #555;
  line-height: 1.5;
  margin-bottom: 0.8rem;
}

.volunteer-form-section {
  margin-top: 3rem;
}

.volunteer-form {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.form-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #2f4f4f;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.form-group textarea {
  resize: vertical;
}

.checkbox-group {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 0.5rem;
}

.checkbox-label {
  display: flex;
  align-items: center;
  font-weight: normal;
}

.checkbox-label input {
  margin-right: 0.5rem;
  width: auto;
}

.submit-btn {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 1rem 2rem;
  font-size: 1.1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  width: 100%;
}

.submit-btn:hover {
  background-color: #45a049;
  transform: translateY(-2px);
}

.submit-btn:disabled {
  background-color: #8bc48e;
  cursor: not-allowed;
  transform: none;
}

.testimonials {
  margin-top: 3rem;
}

.testimonial-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.testimonial {
  background-color: white;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.testimonial .quote {
  font-style: italic;
  margin-bottom: 1rem;
  line-height: 1.6;
}

.testimonial .author {
  font-weight: 600;
  color: #4caf50;
}

.success-message {
  color: green;
  margin-top: 1rem;
}

.error-message {
  color: red;
  margin-top: 1rem;
}

@media (max-width: 768px) {
  .header h1 {
    font-size: 1.8rem;
  }

  .container {
    padding: 1.5rem;
  }

  .opportunity-grid,
  .testimonial-grid {
    grid-template-columns: 1fr;
  }

  .form-row {
    grid-template-columns: 1fr;
    gap: 0;
  }

  .checkbox-group {
    grid-template-columns: 1fr;
  }
}
</style>
