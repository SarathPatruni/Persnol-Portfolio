(function () {
  "use strict";

  var projectOrder = [
    "loan-decision-explanation",
    "loan-approval-prediction",
    "resume-job-matching",
    "warehouse-management",
    "jarvis-ai-assistant"
  ];

  function makeElement(tag, className, text) {
    var element = document.createElement(tag);
    if (className) {
      element.className = className;
    }
    if (text !== undefined) {
      element.textContent = text;
    }
    return element;
  }

  function addSection(parent, title, content, className) {
    var section = makeElement("section", "project-panel " + (className || ""));
    section.appendChild(makeElement("h2", "project-section-title", title));
    section.appendChild(content);
    parent.appendChild(section);
    return section;
  }

  function renderDetails() {
    var root = document.getElementById("project-details");
    if (!root || !window.PORTFOLIO_PROJECTS) {
      return;
    }

    var projectId = document.getElementById("project-detail").getAttribute("data-project-id");
    var project = window.PORTFOLIO_PROJECTS[projectId];
    if (!project) {
      document.title = "Project Not Found | Sarath";
      root.appendChild(makeElement("h1", "project-title", "Project not found"));
      root.appendChild(makeElement("p", "project-intro", "The requested project page could not be found."));
      return;
    }

    document.title = project.title + " | Sarath";
    var header = makeElement("header", "project-detail-header");
    var back = makeElement("a", "project-back-link", "← Back to Projects");
    back.href = "../../index.html#projects";
    header.appendChild(back);
    root.appendChild(header);

    var hero = makeElement("section", "project-hero");
    hero.appendChild(makeElement("p", "project-eyebrow", "PROJECT DETAILS"));
    hero.appendChild(makeElement("h1", "project-title", project.title));
    hero.appendChild(makeElement("p", "project-intro", project.intro));

    var badges = makeElement("div", "project-badges");
    project.technologies.forEach(function (technology) {
      badges.appendChild(makeElement("span", "project-badge", technology));
    });
    hero.appendChild(badges);

    if (project.repository) {
      var repositoryLink = makeElement("a", "project-repository-link", "View GitHub Repository ↗");
      repositoryLink.href = project.repository;
      repositoryLink.target = "_blank";
      repositoryLink.rel = "noopener noreferrer";
      hero.appendChild(repositoryLink);
    }
    root.appendChild(hero);

    if (project.sourceNote) {
      root.appendChild(makeElement("p", "project-source-note", project.sourceNote));
    }

    var summaryGrid = makeElement("div", "project-summary-grid");
    addSection(summaryGrid, "Problem Statement", makeElement("p", "project-copy", project.problem));
    addSection(summaryGrid, "Project Overview", makeElement("p", "project-copy", project.overview));
    root.appendChild(summaryGrid);

    var featureList = makeElement("ul", "project-feature-list");
    project.features.forEach(function (feature) {
      featureList.appendChild(makeElement("li", "", feature));
    });
    addSection(root, "Key Features", featureList);

    addSection(root, "Technical Implementation", makeElement("p", "project-copy", project.implementation));

    var workflow = makeElement("ol", "project-workflow");
    project.workflow.forEach(function (step, index) {
      var item = makeElement("li", "project-workflow-step");
      item.appendChild(makeElement("span", "project-step-number", String(index + 1).padStart(2, "0")));
      item.appendChild(makeElement("span", "project-step-label", step));
      workflow.appendChild(item);
    });
    addSection(root, "Architecture / Workflow", workflow);

    var footer = makeElement("footer", "project-detail-footer");
    var footerBack = makeElement("a", "project-back-link", "← Back to Projects");
    footerBack.href = "../../index.html#projects";
    footer.appendChild(footerBack);
    if (project.repository) {
      var footerRepo = makeElement("a", "project-repository-link", "GitHub Repository ↗");
      footerRepo.href = project.repository;
      footerRepo.target = "_blank";
      footerRepo.rel = "noopener noreferrer";
      footer.appendChild(footerRepo);
    }
    root.appendChild(footer);
  }

  function wireProjectCards() {
    var grid = document.querySelector("#projects .proj-grid");
    if (!grid) {
      return;
    }

    var cards = grid.querySelectorAll(".proj-card");
    Array.prototype.forEach.call(cards, function (card, index) {
      var projectId = projectOrder[index];
      if (!projectId) {
        return;
      }

      var route = "projects/" + projectId + "/";
      var title = card.querySelector(".proj-title");
      card.setAttribute("role", "link");
      card.setAttribute("tabindex", "0");
      card.setAttribute("aria-label", "View details for " + (title ? title.textContent.trim() : "project"));
      card.classList.add("cursor-pointer");

      Array.prototype.forEach.call(card.querySelectorAll("a"), function (link) {
        link.href = route;
        var label = link.querySelector("span");
        if (label) {
          label.textContent = "View Details";
        }
        link.setAttribute("aria-label", "View details for " + (title ? title.textContent.trim() : "project"));
      });

      card.addEventListener("click", function (event) {
        if (event.target.closest("a, button")) {
          return;
        }
        window.location.href = route;
      });
      card.addEventListener("keydown", function (event) {
        if (event.target !== card || (event.key !== "Enter" && event.key !== " ")) {
          return;
        }
        event.preventDefault();
        window.location.href = route;
      });
    });
  }

  renderDetails();
  wireProjectCards();
})();
