$: note("c2 c3 c2 [~ c3] g2 [c2 f2]")
    .s("sawtooth")
    .cutoff(perlin.range(200, 1200).fast(0.5))
    .resonance(15)
    .decay(0.15).sustain(0.1)
    .gain(0.7)

$: note("c4 g4 bb4 d5")
    .s("triangle")
    .fast(2)
    .every(4, x => x.rev())
    .delay(0.4).delaytime(0.25)
    .gain(0.5)

.lpf(2000)

//"I'm looking for something..."
setcpm(30)

RASMUS: stack(

  //wtv_ominous
  note("c3 c4 g4 Bb4 d5 e3").s("sawtooth")
      .transpose(1)
      .lpf(300)
      .orbit(0.8)
      .gain(1)
      .decay(0.5),

  //note_thing
  note("0 4 0 9 7").s("pulse"),

  //underlying
  note("C major  C minor  G major  B major  D minor  Eb minor F ").s("gm_synth_bass_2").crush(6)
     .every(2, x => x.rev().room("<0 .2 .4 .6 .7>"))
     .gain(1.5)
     .echo(1,3,5)
     .transpose(1),

  //first_runner — "I'm looking for something..."
  note("<[[d#4 c4] [a#4 c4] [d#4 c4] [g4 g#4]]>").sound("sin")
      .every(4, x => x.rev().room("<0 .2 .5 .7 .9>"))
      .lpf(slider(1171.9,700,4000))
      .orbit(1)
      .resonance(7)
      .gain(1.2)
      .sustain(0.5).release(0.3).attack(0.2),

  //secondary_melody
  note("c3 c4 g4 bb4 d5 e3")
      .sound("gm_whistle")
      .every(4, x => x.rev().transpose(0.8))
      .orbit(1)
      .mask("<0 1 1 1 0 0 0 1 0 1 >"),

  //second_runner
  note("c2 g2 g3 f4 d3 g3 c3 c2").s("gm_electric_guitar_jazz").fast(1)
      .every(3, x => x.rev())
      .orbit(1)
      .delay(2).delaytime(0.5),

  //nth_melody
  note("c2 g2 g3 c2 d3 g3 c2 e4").s("triangle")
      .fast(1)
      .every(4, x => x.rev())
      .delay(0.4).delaytime(0.25)
      .gain(0.5)
      .orbit(1)
      .resonance(5)
      .mask("<1 1 0 1 0 1 0 1 0 1>"),

  //third_runner
  note("c2 g3 g2 f3 d3 g4 c4 c2").s("pulse").fast(1).add(12)
      .every(3, x => x.rev().early(2))
      .slow(1)
      .orbit(1)
      .delay(2).delaytime(0.5),

  //fourth_runner
  note("c2 g2 g3 c2 d3 g3 c2 e4").s("gm_rock_organ").fast(1)
      .every(2, x => x.rev().slice(1,2))
      .orbit(0.7)
      .echo(1,4,5)
      .delay(3).delaytime(0.5)

)
$: cat(
//TRON
$: cat(
  note("eb5@26 ab4@3 eb5@3"),note("db5@26 ab4@3 db5@3"),
  note("b4@26 ab4@3 b4@3"),note("bb4@26 gb4@3 bb4@3"),note("ab4@29"),
  note("b4@26 ab4@3 b4@3"),note("db5@26 db4@3 eb4@3"),note("ab4@29")
)
.slow(3).s("supersaw").lpf(500)
.room(0.6).gain(1.0)
.transpose(0)
