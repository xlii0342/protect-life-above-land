<template>
  <div class="report-page">
    <header class="header">
      <h1>🐾 Wildlife Report</h1>
    </header>

    <div class="container">
      <div class="intro-card">
        <p>Found an injured, trapped, or endangered animal? Report it to us to help protect Victoria's native species.</p>
        <p>Your report will be forwarded to relevant conservation organizations and wildlife rescuers for timely action.</p>
      </div>
      
      <form class="report-form" @submit.prevent="submitReport">
        <div class="form-group">
          <label for="species">Species (if known)</label>
          <input type="text" id="species" v-model="reportData.species" placeholder="E.g., Kangaroo, Koala, Bird, etc.">
        </div>
        
        <div class="form-group">
          <label for="location">Location</label>
          <input type="text" id="location" v-model="reportData.location" placeholder="Please provide as accurate a location as possible" required>
        </div>
        
        <div class="form-group">
          <label for="date">Date and Time</label>
          <input type="datetime-local" id="date" v-model="reportData.dateTime" required>
        </div>
        
        <div class="form-group">
          <label for="situation">Situation Description</label>
          <textarea id="situation" v-model="reportData.description" rows="4" placeholder="Please describe in detail what you saw and the animal's condition" required></textarea>
        </div>
        
        <div class="form-group">
          <label for="photo">Upload Photo (optional)</label>
          <input type="file" id="photo" @change="handleFileUpload" accept="image/*">
        </div>
        
        <div class="form-group">
          <label for="contact">Contact Information</label>
          <input type="text" id="contact" v-model="reportData.contact" placeholder="Your name and contact details" required>
        </div>
        
        <div class="form-group">
          <button type="submit" class="submit-btn" :disabled="isSubmitting">
            {{ isSubmitting ? 'Submitting...' : 'Submit Report' }}
          </button>
        </div>
      </form>
      
      <div class="emergency-contact">
        <h3>Emergency?</h3>
        <p>If you find a severely injured animal or one in immediate danger, please call immediately:</p>
        <div class="phone-number">
          <strong>Wildlife Emergency Rescue Hotline:</strong> 1300 094 535
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue'

export default {
  name: 'Report',
  components: {
    Footer
  },
  data() {
    return {
      reportData: {
        species: '',
        location: '',
        dateTime: '',
        description: '',
        photo: null,
        contact: ''
      },
      isSubmitting: false
    }
  },
  methods: {
    handleFileUpload(event) {
      this.reportData.photo = event.target.files[0]
    },
    submitReport() {
      this.isSubmitting = true
      
      // Simulate API request
      setTimeout(() => {
        // Successful handling
        this.isSubmitting = false
        alert('Thank you for your report! We will process it as soon as possible.')
        
        // Reset form
        this.reportData = {
          species: '',
          location: '',
          dateTime: '',
          description: '',
          photo: null,
          contact: ''
        }
      }, 2000)
    }
  }
}
</script>

<style scoped>
.report-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.header {
  background-color: #3a6659;
  padding: 2rem;
  border-radius: 10px;
  margin-bottom: 2rem;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
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
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  margin-top: 0;
  margin-bottom: 2rem;
}

.intro-card {
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  margin-bottom: 1.5rem;
}

.intro-card p {
  margin-bottom: 1rem;
  line-height: 1.6;
}

.intro-card p:last-child {
  margin-bottom: 0;
}

.report-form {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  margin-top: 2rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
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
.form-group textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.form-group textarea {
  resize: vertical;
}

.submit-btn {
  background-color: #d35400;
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
  background-color: #ba4a00;
  transform: translateY(-2px);
}

.submit-btn:disabled {
  background-color: #e6876f;
  cursor: not-allowed;
  transform: none;
}

.emergency-contact {
  margin-top: 2rem;
  background-color: #ffe5d9;
  padding: 1.5rem;
  border-radius: 8px;
  border-left: 4px solid #ff6b6b;
}

.emergency-contact h3 {
  color: #d12c1f;
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.emergency-contact p {
  margin-bottom: 0.5rem;
}

.phone-number {
  font-size: 1.1rem;
  padding: 0.5rem 0;
}

@media (max-width: 768px) {
  .header h1 {
    font-size: 1.8rem;
  }
  
  .container,
  .report-form {
    padding: 1.5rem;
  }
}
</style> 