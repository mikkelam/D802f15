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
disp('Probabilities obtained by filtering:');
for i=1:length(data),
   %fprintf('P(R%d=1|e1:%d) = %1.3f\n',i,i,hmm.forwardMessages(1,i));
end

%figure();
%plot(hmm.forwardMessages(1,:));
%xlabel('Time step');
%ylabel('P(R=1|evidence)');