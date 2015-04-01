classdef HMM
    % This class implements a HMM 
    
    properties
        % The number of states in the hidden variable 
        noHidden;
        
        % The number of states in the sensor variable
        noObs;
        
        % Column vector with the prior probabilities over X_0
        priorModel;
        
        % noHidden x noHidden matrix with transModel(i,j)=P(X_t=j|X_{t-1}=i).  
        % That is, the transition probabilities are given row-wise.
        transModel;
                       
        % sensorModel is a cell array with one cell for each state of the sensor variable. 
        % The i'th cell contains a diagonal matrix of size noHidden x
        % noHidden, where the entries correspond to P(e|X), i.e., the
        % likelihoods of the states of X given e.
        sensorModel;          
        
        % Here we store the forward messages.
        forwardMessages;
        
        % Here we store the backward messages.
        backwardMessages;
        
        % Here we store viterbi
        viterbiMessages;
        
        
    end
    
    methods
        
        %% The constructor for the class. 
        % Here we simply initialize the data structures used by the inference algoroithms.
        function obj = HMM(priorModel, transModel, sensorModel)
            obj.priorModel = priorModel;
            obj.transModel = transModel;
            [obj.noHidden, obj.noObs] = size(sensorModel);
            
            % For observation i then sensor model (sensorModel{i}) contains
            % the diagonal matrix with the state likelihoods (see the
            % encoding described in the slides). 
            obj.sensorModel = cell(1,obj.noObs);
            for i = 1:obj.noObs,
                obj.sensorModel{i} = diag(sensorModel(:,i));
            end                                      
            
            obj.forwardMessages = NaN;
            obj.backwardMessages = NaN;
            obj.viterbiMessages = NaN;
        end
        
        
        %% Do forward calculations: P(X_k|e_{1:k})
        function obj = forward(obj, data)
            % Initialization
            totalTime = length(data);
            obj.forwardMessages=zeros(obj.noHidden,totalTime); 
 
            % Do forward calculations    
            % First we handle the initial time step:
            % Do the updating
            obj.forwardMessages(:,1) = obj.sensorModel{data(1)}*obj.priorModel; 
            % and then normalize to ensure that we have a probability
            % distribution
            obj.forwardMessages(:,1) = obj.forwardMessages(:,1)./sum(obj.forwardMessages(:,1));
            % ... and then we consider the remaining ones
            for t=2:totalTime,
                % Do the updating
                obj.forwardMessages(:,t) = obj.sensorModel{data(t)}*obj.transModel'*obj.forwardMessages(:,t-1);                    
                % Normalize
                obj.forwardMessages(:,t) = obj.forwardMessages(:,t)./sum(obj.forwardMessages(:,t));             
            end                 
        end
           
        function obj = backward(obj, data)
            totalTime = length(data);
            
            obj.backwardMessages=zeros(obj.noHidden,totalTime+1);           
            
            obj.backwardMessages(:,totalTime+1) = 1;
            for t=totalTime:-1:1,
                obj.backwardMessages(:,t) = obj.transModel*obj.sensorModel{data(t)}*obj.backwardMessages(:,t+1);
                obj.backwardMessages(:,t) = obj.backwardMessages(:,t)./sum(obj.backwardMessages(:,t));
            end
        end
        
        function obj = viterbi(obj, data)
            obj.forward(data);
            obj.backward(data);
           
            J = obj.forwardMessages .* obj.backwardMessages(:, 1:end-1);
            N = repmat(sum(J), obj.noHidden, 1);
            obj.viterbiMessages = J ./ N
           
        end
                    
        
    end
    
end

