clear all;
close all;

% Transition matrix with transModel(i,j)=P(X_t=j|X_{t-1}=i). I.e., the
% transition probabilities are given row-wise.
transitionModel = [0.7, 0.3;
                   0.3, 0.7];
    
% Column vector with prior probabilities for X_0               
priorModel = [0.5,0.5]';

% Sensor matrx (noHiddenStates x noSensorStates) with the sensor
% probabilities; the sensor probabilities are listed row-wise.
sensorModel = [0.9, 0.1; 
               0.2, 0.8];

% Vector with observations of the sensor variables. States are numbered
% from 1 and onwards.
data = [1, 1, 2, 1, 1];


% Instantiate the HMM class with the probabilities specified above
hmm = HMM(priorModel, transitionModel, sensorModel);

% Perform a filtering operation (forwards pass) with the observations.
hmm=hmm.forward(data);

% backward stuff

hmm=hmm.backward(data);
% Display some results

disp(hmm.backwardMessages);
%disp('Probabilities obtained by filtering:');
%for i=1:length(data),
   %fprintf('P(R%d=1|e1:%d) = %1.3f\n',i,i,hmm.forwardMessages(1,i));
%end

%figure();
%plot(hmm.forwardMessages(1,:));
%xlabel('Time step');
%ylabel('P(R=1|evidence)');

Trans = [ 0.8, 0.2; 
    0.2, 0.8 ];
Prio = [ 0.6, 0.4 ]';
Sens = [ 0.02, 0.21; 
    0.18, 0.49; 
    0.08, 0.09; 
    0.72, 0.21 ]';
% 1=yes+red, 2=yes+not red,  3=no+red, 4=no+not red
% Dat = [ 4, 2, 1 ];

% newhmm = HMM(Prio, Trans, Sens);
% newhmm = newhmm.forward(Dat);
% newhmm = newhmm.backward(Dat);

% disp('Forward:');
% disp(newhmm.forwardMessages);
% disp('Backward:');
% disp(newhmm.backwardMessages);
