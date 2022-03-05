"""// Solver for Destiny 2: Shadowkeep's Xenophage exotic quest puzzles.
// Author: Keegan van der Laag (kvanderlaag@gmail.com)
//
// These are puzzles which have a 3x3 grid of symbols (X,E,V,A), and
// a goal of setting every cell in the grid to the same target symbol.
// Activating one cell of the grid causes every cell in the same row
// and column to advance one symbol in the rotation.
//
// Inputs are given on the command line as "123456789 0", where 1-9 are
// symbols (X, E, V, or A), and 0 is a target symbol. (Also X, E, V, or A.)
// The first sequence corresponds to the starting state of the grid,
// left to right and top to bottom. (The first three symbols are the first
// row, left to right, the second three symbols are the second row, etc.)
//
// If run without any command line arguments, this assumes you wish to solve
// one of the existing puzzles for one of the Lost Sectors on the moon.
// Choose your fighter, and carry on.
//
// The output of this program is the series of symbol positions you need to
// shoot, in order, from the starting state to reach the goal state.
//
// This program will also use ~500MB of memory because it spends a bunch
// of time setting up every possible board state, even though many are
// not reachable from any of the goal states, and thereby should be
// excluded from the possible set. Unfortunately for you, I am very lazy.
// Fortunately for you, this still uses less memory than Discord or Slack
// or some other garbage Electron app. It's 2019, you can deal with it.
//
// If you feel particularly inclined, one could modify this program to
// generate the possible board states outward from the goal state, and
// then do a breadth-first search from there to the initial state. This
// has the added benefit, on top of memory savings, of providing the
// resultant path in the correct order, traversing from the final state
// searched through its parents back to the goal state. This worked fine
// for me, and since this isn't high-performance code, or a job interview,
// I didn't feel the need.
//
// This program makes use of meow hash by Casey Muratori, which can be
// obtained here: https://github.com/cmuratori/meow_hash
// Meow hash is header-only, so you should just need to drop 
// meow_hash_x64_aesni.h into the same folder as this file to compile it.
"""
#include <stdio.h>
#include <vector>
#include <unordered_map>
#include <cassert>
#include <climits>
#include <queue>
#include "meow_hash_x64_aesni.h"


struct State
{
	uint8_t e[3][3];
};

struct Move
{
	uint8_t row;
	uint8_t col;
};

struct Node
{
	State m_state;
	meow_u64 m_stateHash;
	std::unordered_map<uint8_t /* move */, Node* /* destination */> m_links;
	Node* m_parent = nullptr;
	uint8_t m_parentMove = 0;
	bool m_discovered = false;
};

meow_u64 HashState(const State& state)
{
	return MeowU64From(MeowHash(MeowDefaultSeed, 9, (void*)state.e), 0);
}

State DoMove(const State& fromState, const Move& move)
{
	assert(move.col < 3);
	assert(move.row < 3);

	State temp = fromState;

	for (uint8_t y = 0; y < 3; ++y)
	{
		for (uint8_t x = 0; x < 3; ++x)
		{
			if (x == move.col || y == move.row)
			{
				uint8_t& inSym = temp.e[y][x];

				switch (inSym)
				{
				case 'X':
					inSym = 'E';
					break;
				case 'E':
					inSym = 'V';
					break;
				case 'V':
					inSym = 'A';
					break;
				case 'A':
					inSym = 'X';
					break;
				}

			}
		}
	}
	return temp;
}

int main(int argc, char** argv)
{
	if (argc != 3 && argc != 1)
	{
		printf("Usage:\n\n Interactive mode: xenophage.exe\nManual input: nnnnnnnnn m, where n is a symbol (X,E,V,A), and m is a target symbol for the grid.\n");
		return -1;
	}

	std::string grid;
	char target;

	if (argc == 1)
	{
		char inputChar;
		bool selected = false;
		while (!selected)
		{
			printf("Select Lost Sector:\n1) K1 Logistics\n2) K1 Crew\n3) K1 Revelation\n4) K1 Communion\n> ");
			inputChar = getchar();
			switch (inputChar)
			{
			case '1':
				grid = "EEEAEEEEE";
				target = 'A';
				selected = true;
				break;
			case '2':
				grid = "AXVAXXAAA";
				target = 'E';
				selected = true;
				break;
			case '3':
				grid = "EAVVXVEAV";
				target = 'X';
				selected = true;
				break;
			case '4':
				grid = "AXAEXEXVX";
				target = 'V';
				selected = true;
				break;
			default:
				printf("Invalid Selection.\n\n");
				inputChar = 0;
			}
		}
	}
	else
	{
		grid.assign(argv[1]);

		if (grid.length() != 9)
		{
			printf("Grid input length incorrect, must be 9 symbols. (3x3)\n");
			return -1;
		}

		target = argv[2][0];

		switch (target)
		{
		case 'X':
		case 'E':
		case 'V':
		case 'A':
			break;
		default:
			printf("Invalid target symbol, symbol must be X, E, V, or A\n");
			return -1;
		}
	}	

	State startState;
	for (int row = 0; row < 3; ++row)
	{
		for (int col = 0; col < 3; ++col)
		{
			switch (grid[row * 3 + col])
			{
			case 'X':
			case 'E':
			case 'V':
			case 'A':
				startState.e[row][col] = grid[row * 3 + col];
				break;
			default:
				printf("Invalid input symbol in grid, symbols must be X, E, V, or A\n");
				return -1;
			}
		}
	}

	State goalState;
	for (int row = 0; row < 3; ++row)
	{
		for (int col = 0; col < 3; ++col)
		{
			goalState.e[row][col] = target;
		}
	}

	meow_u64 startHash = HashState(startState);
	meow_u64 goalHash = HashState(goalState);

	// Create graph

	printf("Initializing Data...\n");

	std::unordered_map<meow_u64, Node> graph;
	{
		struct row
		{
			uint8_t e[3];
		};

		std::vector<row> rowPermutations;
		rowPermutations.push_back({ 'X','X','X' });
		rowPermutations.push_back({ 'X','X','E' });
		rowPermutations.push_back({ 'X','X','V' });
		rowPermutations.push_back({ 'X','X','A' });
		rowPermutations.push_back({ 'X','E','X' });
		rowPermutations.push_back({ 'X','E','E' });
		rowPermutations.push_back({ 'X','E','V' });
		rowPermutations.push_back({ 'X','E','A' });
		rowPermutations.push_back({ 'X','V','X' });
		rowPermutations.push_back({ 'X','V','E' });
		rowPermutations.push_back({ 'X','V','V' });
		rowPermutations.push_back({ 'X','V','A' });
		rowPermutations.push_back({ 'X','A','X' });
		rowPermutations.push_back({ 'X','A','E' });
		rowPermutations.push_back({ 'X','A','V' });
		rowPermutations.push_back({ 'X','A','A' });

		rowPermutations.push_back({ 'E','X','X' });
		rowPermutations.push_back({ 'E','X','E' });
		rowPermutations.push_back({ 'E','X','V' });
		rowPermutations.push_back({ 'E','X','A' });
		rowPermutations.push_back({ 'E','E','X' });
		rowPermutations.push_back({ 'E','E','E' });
		rowPermutations.push_back({ 'E','E','V' });
		rowPermutations.push_back({ 'E','E','A' });
		rowPermutations.push_back({ 'E','V','X' });
		rowPermutations.push_back({ 'E','V','E' });
		rowPermutations.push_back({ 'E','V','V' });
		rowPermutations.push_back({ 'E','V','A' });
		rowPermutations.push_back({ 'E','A','X' });
		rowPermutations.push_back({ 'E','A','E' });
		rowPermutations.push_back({ 'E','A','V' });
		rowPermutations.push_back({ 'E','A','A' });

		rowPermutations.push_back({ 'V','X','X' });
		rowPermutations.push_back({ 'V','X','E' });
		rowPermutations.push_back({ 'V','X','V' });
		rowPermutations.push_back({ 'V','X','A' });
		rowPermutations.push_back({ 'V','E','X' });
		rowPermutations.push_back({ 'V','E','E' });
		rowPermutations.push_back({ 'V','E','V' });
		rowPermutations.push_back({ 'V','E','A' });
		rowPermutations.push_back({ 'V','V','X' });
		rowPermutations.push_back({ 'V','V','E' });
		rowPermutations.push_back({ 'V','V','V' });
		rowPermutations.push_back({ 'V','V','A' });
		rowPermutations.push_back({ 'V','A','X' });
		rowPermutations.push_back({ 'V','A','E' });
		rowPermutations.push_back({ 'V','A','V' });
		rowPermutations.push_back({ 'V','A','A' });

		rowPermutations.push_back({ 'A','X','X' });
		rowPermutations.push_back({ 'A','X','E' });
		rowPermutations.push_back({ 'A','X','V' });
		rowPermutations.push_back({ 'A','X','A' });
		rowPermutations.push_back({ 'A','E','X' });
		rowPermutations.push_back({ 'A','E','E' });
		rowPermutations.push_back({ 'A','E','V' });
		rowPermutations.push_back({ 'A','E','A' });
		rowPermutations.push_back({ 'A','V','X' });
		rowPermutations.push_back({ 'A','V','E' });
		rowPermutations.push_back({ 'A','V','V' });
		rowPermutations.push_back({ 'A','V','A' });
		rowPermutations.push_back({ 'A','A','X' });
		rowPermutations.push_back({ 'A','A','E' });
		rowPermutations.push_back({ 'A','A','V' });
		rowPermutations.push_back({ 'A','A','A' });

		for (const auto& row1 : rowPermutations)
		{
			for (const auto& row2 : rowPermutations)
			{
				for (const auto& row3 : rowPermutations)
				{
					Node node;

					node.m_state.e[0][0] = row1.e[0];
					node.m_state.e[0][1] = row1.e[1];
					node.m_state.e[0][2] = row1.e[2];

					node.m_state.e[1][0] = row2.e[0];
					node.m_state.e[1][1] = row2.e[1];
					node.m_state.e[1][2] = row2.e[2];

					node.m_state.e[2][0] = row3.e[0];
					node.m_state.e[2][1] = row3.e[1];
					node.m_state.e[2][2] = row3.e[2];

					node.m_stateHash = HashState(node.m_state);
					graph.insert({ node.m_stateHash, std::move(node) });
				}
			}
		}
	}

	for (auto& node : graph)
	{
		for (uint8_t row = 0; row < 3; ++row)
		{
			for (uint8_t col = 0; col < 3; ++col)
			{
				auto foundNode = graph.find(HashState((DoMove(node.second.m_state, { row, col }))));
				assert(foundNode != graph.end());

				node.second.m_links.insert({
					((row & 3) << 2) + (col & 3),
					&(foundNode->second) }
				);
			}
		}
		assert(node.second.m_links.size() == 9);
	}

	auto goalIterator = graph.find(goalHash);
	assert(goalIterator != graph.end());

	std::queue<meow_u64> path;
	path.push(startHash);
	auto v = graph.find(startHash);
	v->second.m_discovered = true;

	while (!path.empty())
	{
		v = graph.find(path.front());
		path.pop();

		if (v->second.m_stateHash == goalHash)
		{
			break;
		}

		for (auto& link : v->second.m_links)
		{
			if (!link.second->m_discovered)
			{
				link.second->m_discovered = true;
				link.second->m_parent = &(v->second);
				link.second->m_parentMove = link.first;
				path.push(link.second->m_stateHash);
			}
		}
	}

	std::vector<uint8_t> moves;

	Node& step = goalIterator->second;
	while (step.m_parent != nullptr)
	{
		moves.push_back(step.m_parentMove);
		step = *step.m_parent;
	}

	while (!moves.empty())
	{
		uint8_t row = moves.back() >> 2;
		uint8_t col = moves.back() & 3;

		std::string rowStr, colStr;

		switch (row)
		{
		case 0:
			rowStr = "Top";
			break;
		case 1:
			rowStr = "Middle";
			break;
		case 2:
			rowStr = "Bottom";
			break;
		}

		switch (col)
		{
		case 0:
			colStr = "Left";
			break;
		case 1:
			colStr = "Middle";
			break;
		case 2:
			colStr = "Right";
			break;
		}

		printf("%s %s\n", rowStr.c_str(), colStr.c_str());
		moves.pop_back();
	}
	return 0;
}