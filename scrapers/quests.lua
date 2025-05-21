local function exportToFiles(list, data)
	for questID, questInfo in pairs(list) do
		if type(data[questID]) == "table" then
			print("Quest ID: " .. tostring(questID))
			print("Title: " .. data[questID]["T"])

			local file = io.open("../corpus/quests/" .. tostring(questID) .. ".md", "w")
			if file then
				file:write("Quest ID: " .. tostring(questID) .. "\n")
				file:write("Level: " .. tostring(questInfo["lvl"]) .. "\n")
				file:write("Min Level: " .. tostring(questInfo["min"]) .. "\n")
				file:write("Race: " .. tostring(questInfo["race"]) .. "\n")
				file:write("Title: " .. data[questID]["T"] .. "\n")
				file:write("Description: " .. data[questID]["D"] .. "\n")
				file:write("Objective: " .. data[questID]["O"] .. "\n")
				file:close()
			else
				print("Error: Could not open file for writing.")
			end
		end
	end
end

-- Export Vanilla Quests
do
	local list = require("quests-vanilla.quests")
	local data = require("quests-vanilla.enUS.quests")
	exportToFiles(list, data)
end

-- Export Turtle Quests
do
	local list = require("quests-turtle.quests-turtle")
	local data = require("quests-turtle.enUS.quests-turtle")
	exportToFiles(list, data)
end

