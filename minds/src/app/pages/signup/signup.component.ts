import { Component, OnInit, ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  recognition;
  answers = {};
  answering = false;
  questions: Question[] = [
    {
      getQuestion: () => 'Hello! Nice to meet you, what is your name?',
      answerKey: 'name'
    },
    {
      getQuestion: () => `That is a nice name, ${this.answers['name']}! How old are you?`,
      answerKey: 'age'
    },
    {
      getQuestion: () => 'That’s nice! Do you know where you stay?',
      answerKey: 'location'
    },
    {
      getQuestion: () => 'What do you like to do?',
      answerKey: 'jobs'
    }
  ];
  currentQuestionIndex = 0;
  current: Question = this.questions[this.currentQuestionIndex];

  constructor(private changeDetector: ChangeDetectorRef) { }

  ngOnInit() {
    const {webkitSpeechRecognition}: IWindow = <IWindow>window;
    this.recognition = new webkitSpeechRecognition();
    this.recognition.lang = 'en-GB';
    this.recognition.continuous = true;
    this.recognition.onresult = (event) => {
      this.recognition.stop();
      const text = event.results[0][0].transcript;
      this.onAnswer(text);
      this.changeDetector.detectChanges();
    };
  }

  onAnswer(answer) {
    console.log(answer);
    this.answering = false;
    this.answers[this.questions[this.currentQuestionIndex].answerKey] = answer;
    this.currentQuestionIndex += 1;
    this.current = this.questions[this.currentQuestionIndex];
  }

  startAnswer() {
    this.recognition.start();
    this.answering = true;
    this.changeDetector.detectChanges();
  }

}

export interface IWindow extends Window {
  webkitSpeechRecognition: any;
}

export interface Question {
  getQuestion: () => string;
  answerKey: string;
}
