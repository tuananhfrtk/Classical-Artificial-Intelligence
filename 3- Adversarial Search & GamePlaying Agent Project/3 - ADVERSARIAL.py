
from sample_players import DataPlayer
import random

class CustomPlayer(DataPlayer):
    def __init__(self, player_id):
        super().__init__(player_id)
        self.killer_moves = {}
     


    def get_action(self, state):
        
        
        if self.context is None:
            self.context = {'node': 0, 'layer': 0}
            
        if state.ply_count < 2:
            self.queue.put(random.choice(state.actions())) 
                        
        else:
            depth = 1
        while True:
            node = self.context['node']
            self.queue.put(self.alpha_beta_search(state, depth, self.combined))
            self.context['layer'] += depth
                
                # terminate if no new nodes are found
            if self.context['node'] - node == depth:
                return
            depth += 1

#-------------KILLER HEURISTICS + ALPHA-BETA PRUNING
        
    def alpha_beta_search(self, state, depth, heuristic):
    
        def __init__(self):
            self.killer_moves = {}  

        def min_value(state, depth, alpha, beta, d):
            self.context['node'] += 1

            if state.terminal_test():
                return state.utility(self.player_id)

            if depth == 0:
                return heuristic(state)
        
            v = float("inf")
        
        
            actions = state.actions()
            if d in self.killer_moves:
                actions = self.killer_moves[d] + [a for a in actions if a not in self.killer_moves[d]]      
        
        
            for action in actions:
                v = min(v, max_value(state.result(action), depth - 1, alpha, beta, d + 1))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v 
            
        def max_value(state, depth, alpha, beta, d):
            self.context['node'] += 1

            if state.terminal_test():
                return state.utility(self.player_id)
            
            if depth == 0: 
                return heuristic(state)

            v = float("-inf")
            
            actions = state.actions()
            if d in self.killer_moves:
                actions = self.killer_moves[d] + [a for a in actions if a not in self.killer_moves[d]]              
        
            for action in actions:
                v = max(v, min_value(state.result(action), depth - 1, alpha, beta, d + 1))
                if v >= beta:
                    if d not in self.killer_moves:
                        self.killer_moves[d] = []
                    if action not in self.killer_moves[d]:
                        self.killer_moves[d].insert(0, action)
                        if len(self.killer_moves[d]) > 2:  # Keep the two best moves
                            self.killer_moves[d].pop()
                    return v
                alpha = max(alpha, v)
            return v
                                
        alpha = float('-inf')
        beta = float('inf')
        best_score = float('-inf')
        best_move = state.actions()[0]
        for action in state.actions():
            v = min_value(state.result(action), depth - 1, alpha, beta, 1)
            if v > best_score:
                best_score = v
                best_move = action
            alpha = max(alpha, v) 
        return best_move      

#------------------------------------ADVANCED HEURISTICS                 

    def baseline(self, state):
        """ baseline function given in project introduction using the #my_moves - #opponent_moves 
        heuristics."""
        my_liberties = len(state.liberties(state.locs[self.player_id]))
        opponent_liberties = len(state.liberties(state.locs[1 - self.player_id]))
        return my_liberties - opponent_liberties
    
    def central(self, state):
        """Evaluate the state based on proximity to the center and edge effects."""
        
        # Get player positions
        pos_1 = state.locs[self.player_id]
        pos_2 = state.locs[1 - self.player_id]

        # Convert linear position to 2D coordinates (assuming an 11x9 board)
        x1, y1 = divmod(pos_1, 11)  # Coordinates of player 1
        x2, y2 = divmod(pos_2, 11)  # Coordinates of player 2

        # Center of the board
        center_x, center_y = 5, 4

        # Calculate distance to the center
        distance1 = ((x1 - center_x) ** 2 + (y1 - center_y) ** 2)
        distance2 = ((x2 - center_x) ** 2 + (y2 - center_y) ** 2)

        # Penalize positions close to the edges
        edge_penalty1 = max(abs(x1 - 0), abs(x1 - 10), abs(y1 - 0), abs(y1 - 8))
        edge_penalty2 = max(abs(x2 - 0), abs(x2 - 10), abs(y2 - 0), abs(y2 - 8))

        # Weighted centrality
        center_value = -(distance1 - 2 * edge_penalty1) + (distance2 - 2 * edge_penalty2)
        
        return center_value
    
    def combined(self, state):
        """Combine baseline and central heuristics with weighted coefficients."""
        return 0.5 * self.Baseline(state) + 1.5 * self.Central(state)
     
          
      



    

 
  
  
  
  

  

