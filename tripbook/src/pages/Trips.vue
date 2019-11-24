<template>
  <q-page padding>
    <div class="q-pa-md">
      <q-stepper
        v-model="step"
        ref="stepper"
        color="primary"
        animated
      >
        <q-step
          :name="1"
          title="Where do you want to go?"
          icon="trip_origin"
          :done="step > 1"
        >
          <div class="text-h6 q-mx-lg q-pb-none">How does it look like?</div>
          <div class="text-caption text-italic q-mx-lg q-pt-none">
            Upload some of the photos of landscapes, monuments and views that
            you like the most?
          </div>
          <vue-dropzone
            ref="myVueDropzone"
            id="dropzone"
            class="q-ma-lg"
            :duplicateCheck="true"
            :options="dropzoneOptions"
            :useCustomSlot="true"
          >
            <div class="dropzone-custom-content">
              <q-icon
                name="cloud_upload"
                size="12vw"
              ></q-icon>
              <div class="text-h3">Drag and drop to upload content!</div>
              <div class="subtitle">...or click to select a file from your computer</div>
            </div>
          </vue-dropzone>
        </q-step>

        <q-step
          :name="2"
          title="When do you plan this trip?"
          icon="date_range"
          :done="step > 2"
        >
          <div>
            <div class="text-h6 q-mx-lg q-pb-none">Would you like to describe it?</div>
            <div class="text-caption text-italic q-mx-lg q-pt-none">Some prefers land, some enjoy beaches, what about you dear user?</div>
            <div class="q-mx-lg row q-col-gutter-md q-my-lg">
              <q-input
                class="col-xs-6 col-md-4"
                rounded
                outlined
                v-model="country"
                label="Country"
              />
              <q-input
                class="col-xs-6 col-md-4"
                rounded
                outlined
                v-model="touristic"
                label="Touristic Views"
              />
              <q-input
                class="col-xs-6 col-md-4"
                rounded
                outlined
                v-model="keywords"
                label="Keywords"
              />
            </div>
            <br />
            <div class="text-h6 q-mx-lg q-pb-none">When would you like to start this adventure?</div>
            <div class="text-caption text-italic q-mx-lg q-pt-none">
              Optionally you can provide some dates to fit with the best Offers
              we can match?
            </div>
            <div class="row q-pa-md q-ma-lg justify-center q-col-gutter-x-lg">
              <q-input
                label="From"
                class="col-4"
                filled
                v-model="startDate"
              >
                <template v-slot:prepend>
                  <q-icon
                    name="event"
                    class="cursor-pointer"
                  >
                    <q-popup-proxy
                      transition-show="scale"
                      transition-hide="scale"
                    >
                      <q-date
                        v-model="startDate"
                        mask="YYYY-MM-DD HH:mm"
                      />
                    </q-popup-proxy>
                  </q-icon>
                </template>

                <template v-slot:append>
                  <q-icon
                    name="access_time"
                    class="cursor-pointer"
                  >
                    <q-popup-proxy
                      transition-show="scale"
                      transition-hide="scale"
                    >
                      <q-time
                        v-model="startDate"
                        mask="YYYY-MM-DD HH:mm"
                        format24h
                      />
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
              <q-input
                label="To"
                class="col-4"
                filled
                v-model="endDate"
              >
                <template v-slot:prepend>
                  <q-icon
                    name="event"
                    class="cursor-pointer"
                  >
                    <q-popup-proxy
                      transition-show="scale"
                      transition-hide="scale"
                    >
                      <q-date
                        v-model="endDate"
                        mask="YYYY-MM-DD HH:mm"
                      />
                    </q-popup-proxy>
                  </q-icon>
                </template>

                <template v-slot:append>
                  <q-icon
                    name="access_time"
                    class="cursor-pointer"
                  >
                    <q-popup-proxy
                      transition-show="scale"
                      transition-hide="scale"
                    >
                      <q-time
                        v-model="endDate"
                        mask="YYYY-MM-DD HH:mm"
                        format24h
                      />
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
            </div>
          </div>
        </q-step>

        <q-step
          :name="3"
          style="height: 75vh"
          title="Pick a flavour!"
          icon="loyalty"
        >
          <div class="row justify-center">

            <div class="col-12 justify-start">

              <q-inner-loading :showing="loading">
                <img src="../assets/wedgesloader.gif" />
              </q-inner-loading>
              <div
                class="text-h6 q-mx-lg q-pb-none"
                v-if="!loading"
              >Select your favourite Destination</div>
              <div
                v-if="!loading"
                class="text-caption text-italic q-mx-lg q-pt-none"
              >
                According to the photos you have provided, we suggest following
                destinations for you, select one to proceed...
              </div>

            </div>
            <div
              class="col-8"
              v-if="!loading"
            >
              <carousel-3d
                class="justify-center items-center"
                style="height: 50vh!important;"
              >
                <slide
                  style="height:auto!important;"
                  class="col-12"
                  v-for="(slide, i) in slides"
                  :index="i"
                  :key="i"
                >
                  <template slot-scope="{ index, isCurrent, leftIndex, rightIndex }">
                    <q-card style="min-height: 40px">
                      <img
                        :data-index="index"
                        :class="{
                      current: isCurrent,
                      onLeft: leftIndex >= 0,
                      onRight: rightIndex >= 0
                    }"
                        @click="CarouselIndex = slide"
                        src="https://cdn.quasar.dev/img/mountains.jpg"
                      />
                      <q-card-actions align="around">
                        <q-btn
                          flat
                          round
                          color="red"
                          icon="favorite"
                        />
                        <q-btn
                          flat
                          round
                          color="teal"
                          icon="bookmark"
                        />
                        <q-btn
                          flat
                          round
                          color="primary"
                          icon="share"
                        />
                      </q-card-actions>
                    </q-card>
                  </template>
                </slide>
              </carousel-3d>

              <div class="text-h6 q-mt-none">
                Description
              </div>
              <div class="q-pa-md text-italic">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias, aut saepe. Architecto, corrupti iste! Id et libero qui suscipit, mollitia ut necessitatibus ratione eos, quae ipsa sequi natus, quos facilis.
              </div>
            </div>
            <div
              class="col-3"
              v-if="!loading"
            >
              <q-card class="my-card">
                <q-card-section>
                  <q-carousel
                    animated
                    v-model="slide"
                    arrows
                    navigation
                    infinite
                  >
                    <q-carousel-slide
                      :name="1"
                      img-src="https://cdn.quasar.dev/img/mountains.jpg"
                    />
                    <q-carousel-slide
                      :name="2"
                      img-src="https://cdn.quasar.dev/img/parallax1.jpg"
                    />
                    <q-carousel-slide
                      :name="3"
                      img-src="https://cdn.quasar.dev/img/parallax2.jpg"
                    />
                    <q-carousel-slide
                      :name="4"
                      img-src="https://cdn.quasar.dev/img/quasar.jpg"
                    />
                  </q-carousel>
                </q-card-section>

                <q-card-section>
                  <div class="text-h6">Photos of {{CarouselIndex}}</div>
                  <q-rating
                    size="24px"
                    v-model="stars"
                    :max="5"
                  />
                </q-card-section>
              </q-card>

            </div>
          </div>

        </q-step>

        <q-step
          :name="4"
          title="Get some Credit"
          icon="money"
        >
          <div class="q-pa-md q-gutter-md">
            <div class="row justify-between">

              <q-parallax>
                <template v-slot:media>
                  <img src="../assets/hand_transfer.png">
                </template>

                <template v-slot:content="scope">
                  <div
                    class="absolute column items-center"
                    :style="{
                      opacity: 0.45 + (1 - scope.percentScrolled) * 0.55,
                      top: (scope.percentScrolled * 60) + '%',
                      left: 0,
                      right: 0
                    }"
                  >
                    <img
                      src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg"
                      style="width: 150px; height: 150px"
                    >
                    <div class="text-h3 text-white text-center">Quasar Framework</div>
                    <div class="text-h6 text-grey-3 text-center">
                      v{{ $q.version }}
                    </div>
                  </div>
                </template>
                <!-- <div class="text-h6 q-mx-lg q-pb-none">Enhance your adventure with the Libra Experience?</div>
                <div class="text-caption text-italic q-mx-lg q-pt-none">
                  Facebook provides you with the Libra Credit, A trustworthy payment
                  system for your purchases.
                </div> -->
              </q-parallax>

            </div>
          </div>
          <!-- <div class="text-h6 q-mx-lg q-pb-none">Enhance your adventure with the Libra Experience?</div>
          <div class="text-caption text-italic q-mx-lg q-pt-none">
            Facebook provides you with the Libra Credit, A trustworthy payment
            system for your purchases.
          </div> -->
          <!--          <q-img src="../assets/hand_transfer.png"/>-->
          <!-- <div class="row q-col-gutter-lg q-pa-lg">
            <div class="col-4">
              <q-slider
                v-model="libraCredit"
                :min="0"
                :max="2000"
                :step="1"
                label
                label-always
                color="light-green"
              />
            </div>
            <img
              class="col-6"
              src="../assets/hand_transfer.png"
            />
          </div> -->
        </q-step>

        <template v-slot:navigation>
          <q-stepper-navigation>
            <q-btn
              @click="$refs.stepper.next()"
              color="primary"
              :label="step === 4 ? 'Finish' : 'Continue'"
            />
            <q-btn
              v-if="step > 1"
              flat
              color="primary"
              @click="$refs.stepper.previous()"
              label="Back"
              class="q-ml-sm"
            />
          </q-stepper-navigation>
        </template>
      </q-stepper>
    </div>
  </q-page>
</template>

<script>
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import { Carousel3d, Slide } from 'vue-carousel-3d'

export default {
  name: 'TipsPage',
  components: {
    vueDropzone: vue2Dropzone,
    Carousel3d,
    Slide
  },
  methods: {
    loadFlavours () {
      this.loading = true
      setTimeout(() => {
        this.loading = false
      }, 1500)
    }
  },
  watch: {
    step (nv) {
      if (nv === 3) this.loadFlavours()
    }
  },
  data: function () {
    return {
      dropzoneOptions: {
        url: 'https://httpbin.org/post',
        thumbnailWidth: 150,
        acceptedFiles: 'image/*',
        addRemoveLinks: true,
        maxFilesize: 0.5,
        headers: { 'My-Awesome-Header': 'header value' }
      },
      CarouselIndex: 1,
      country: '',
      startDate: null,
      endDate: null,
      touristic: '',
      keywords: '',
      loading: false,
      step: 3,
      stars: 4.5,
      slides: 7,
      slide: 1,
      libraCredit: 100
    }
  }
}
</script>
